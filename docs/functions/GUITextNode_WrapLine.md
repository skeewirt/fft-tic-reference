# GUITextNode_WrapLine

- **Address:** `0x1403DE608`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned __int64 GUITextNode_WrapLine(GUITextLayout *layout, GUITextLayoutState *st)`
- **Callers:** GUITextNode_PlaceGlyph (tail call, when node+260 = 0 and rec.x + width > W), GUITextNode_PlaceIcon (same test for an inline icon)
- **Callees:** sub_1400796D0 (UTF-8 decode of next), GUITextNode_FinishLine, allocator vtable +16 / +24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Word wrap: when the glyph just placed does not fit the node width, finds the last line-break opportunity in the current line, finishes the line before it (soft-wrap flag set) and starts a new line with the glyphs after it.

## Behavior

- V (arguments): layout and st as in GUITextNode_FinishLine. Locals: n = st+64 (glyphs of the current line; they are the last n 36-byte records of the glyph vector at layout+8 / +16), next = the character decoded from the string at st+16 (the character AFTER the one just placed; only the French / German rules use it; the Hex-Rays text shows it as 0, the disassembly loads it from the decoder's output slot), j = number of trailing glyphs to move (starts at 1).
- V (scan, runs while j < n): left = glyph record [count - 1 - j], right = record [count - j]; right starts as the last (overflowing) glyph. The scan stops with j when a break is allowed between left and right, otherwise j += 1 and left becomes the new right. It always stops (no break) when left.char (+20) is 0 or right.char is 0 (an inline icon record, see GUITextNode_PlaceIcon).
- V (rules when layout+123 = 0, i.e. not Japanese / Chinese): break when left is '-' (45) or an en dash (8211). If layout+121 (French and German only): also break when left is an em dash (8212) or a soft hyphen (173); and when right is a space: no language object = break; French (language 2) = no break when next is one of ! ? ; : % >> (U+00BB, U+226B, U+300B) or when left is one of << (U+00AB, U+226A, U+300A), otherwise break; German (language 3) = no break when next is '.', otherwise break; right not a space = keep scanning. If layout+121 is 0 (English and the rest): break when left is 8212 or 173, or right is a space (32). A no-break space (160) is not 32, so it never breaks here.
- V (rules when layout+123 = 1, Japanese / Simplified / Traditional Chinese): no break when right is in the 78-entry list at 0x1406FDFD0 (closing brackets and quotes, ! ?, : ;, full stops, commas, small kana, the long vowel mark, ellipsis) or left is in the 20-entry opening-bracket list at 0x1406FE070; no break between two equal characters of the list at 0x1406FE0A0 (em dash, two-dot leader, ellipsis); no break when either character is 160. Any other pair is a break (so CJK text breaks between any two glyphs).
- V (nothing found, j reached n): j = 0 when n is 1, else j = 1, i.e. a single over-long word is split by moving only the last glyph to the new line. A single glyph in the line is never moved (the line is closed with it).
- V (move): the last j glyph records are popped off the glyph vector into a temporary vector (reversed order) and st+64 -= j. If the first moved glyph (the one that was popped last) is a space (char 32) it is dropped from the temporary vector, so a wrapped line does not start with a space.
- V (close the old line): st+88 = 1 then GUITextNode_FinishLine(layout, st), which aligns / justifies the remaining glyphs, appends the line record (+21 = 1) and advances the y cursor (it also clears st+88, st+36 and st+64).
- V (open the new line): the moved records are appended back in text order with x = x - x of the first kept moved glyph (so the line starts at x 0) and +24 (line index) = the current line count; st+64 = number of re-added glyphs; st+36 (pen) = last.x + last.width. When st+90 is 0 and the last re-added glyph is a soft hyphen (173) and there are at least 2 glyphs, the pen is the previous glyph's x + width instead (the soft hyphen does not advance).
- V: the temporary vector is allocated and freed through the allocator at qword_143CDAA80 + 32 (vtable +16 allocate, +24 free); the glyph vector grows through the layout allocator the same way.
- I: the wrap is checked once per placed glyph by the caller; after one wrap the rebased line can still be wider than W only for a single glyph, which is then closed alone by the next wrap call.

## State touched

- Calls: [GUITextNode_FinishLine](GUITextNode_FinishLine.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [GUITextNode_PlaceIcon](GUITextNode_PlaceIcon.md)

## Notes

The name is ours (IDB: sub_1403DE608). Wrap only runs for overflow mode node+260 = 0; with modes 2 (shrink) or 3 it never runs. For a single-line text that fits (every glyph rec.x + width <= W) it is never entered.

## Open questions

? whether st+90 (soft-hyphen-suppress) is ever set outside the tag handler (not traced). ? the exact semantics of the French lists were read from the decompile (the Hex-Rays nesting of the inner `break` statements was resolved by hand and should be re-checked on a live French string). ? the CJK lists were dumped as code points only, not named one by one.
