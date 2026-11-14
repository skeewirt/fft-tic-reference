# GUITextNode_FinishLine

- **Address:** `0x1403DDED8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUITextNode_FinishLine(GUITextLayout *layout, GUITextLayoutState *st)`
- **Callers:** sub_1403DD3A0 (6 call sites: line-break tag handling), GUITextNode_AlignVertical, sub_1403DE608 (soft wrap)
- **Callees:** UITable_GetRow, sub_1403A942C (italic shear width), allocator vtable +16 / +24 for growing the line vector

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Closes the current text line: measures it, applies the overflow rule and the horizontal alignment to the line's glyph records, adjusts each glyph's y for the font baseline term, appends the 24-byte line record and advances the y cursor.

## Behavior

- V (arguments): layout (a1) holds the glyph vector (+8 begin, +16 end, +24 capacity; 36-byte records) and the line vector (+40 begin, +48 end, +56 capacity; 24-byte records), the allocator at +32, and the language flags set by GUITextNode_Layout (+122 always 0, +123 = Japanese / Simplified / Traditional Chinese). st (a2) is the layout state built on GUITextNode_Layout's stack: +0 node, +32 UIFontType id, +36 pen x, +40 line y cursor, +64 number of glyphs of the current line (they are the LAST st+64 records of the glyph vector), +85 horizontal alignment (node+252, 4 replaced by 0 for Korean), +88 soft-wrap flag (set to 1 only by sub_1403DE608, cleared here). Locals: size = (float)(int16 node+304), W = (float)(int32 node+64), K = UIFontType row (UITable_GetRow(27, st+32)) +8 (Unknown8) * 0.015625 (0 when the row is missing).
- V (line width): lineWidth = max over the line's glyphs of (rec.x + rec.width). When the renderer's shear (renderer+9524) is > 0 and the last glyph's italic byte (+29) is set, lineWidth = max + S * last.f, with S = sub_1403A942C = (font +232 * renderer+9500) * (shear * 96 * 0.5) (0 when renderer+189 is 0). I: S is the extra width the sheared top of an italic glyph needs.
- V (overflow, node+260): when lineWidth > W, value 2 (shrink): squeeze = W / lineWidth, lineWidth = W, and every glyph of the line gets x = x * squeeze and width = width * squeeze; value 3: only the line flag (+20) is set to 1; other values do nothing here (value 0 wraps earlier, in GUITextNode_PlaceGlyph).
- V (horizontal alignment a = st+85): a = 4 (auto) with the soft-wrap flag set goes to the justify path; a = 4 without it becomes 2 (right) if layout+122 else 0 (left); 0 = left (x offset 0); 1 = centre, x offset (W - lineWidth) / 2; 2 = right, W - lineWidth; 3 = distribute: spacing d = (W - lineWidth) / (nGlyphs - 1) added between glyphs, a single glyph is centred; any other value = left. The justify path (a = 4 + soft wrap) is distribute when layout+123 is set (CJK), otherwise space justify: spaces = number of glyphs with char 32, per-space extra e = (W - lineWidth) / spaces, no spaces = centred. Distribute and justify set lineWidth = W.
- V (per glyph i of the line, in order): rec.x += (spaces before i) * e + i * d; rec.y += K * size - (size * rec.f) * K (so the later pen y of GUITextNode_Draw, which adds K * size * f, comes out at K * size for every f); a soft hyphen (char 173) becomes 32 unless it is the last glyph of the line, where it becomes 45 (hyphen-minus).
- V (line record appended at layout+40, 24 bytes): +0 x offset (the alignment value above, 0 for left), +4 y = st+40 (the cursor before this line), +8 width = lineWidth (W when shrunk, distributed or justified), +12 height = size, +16 x-squeeze (1.0 unless shrunk), +20 byte flag (overflow 3 and lineWidth > W), +21 byte = st+88 (soft wrap).
- V (cursor): st+36 = 0, st+64 = 0, st+88 = 0, st+40 = size + (int16 node+308) + st+40. So the line pitch is the node's size plus the node's int16 +308 (UIB line spacing), not the font's line height.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md)
- Reads: [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUITextNode_AlignVertical](GUITextNode_AlignVertical.md), [GUITextNode_HandleTag](GUITextNode_HandleTag.md), [GUITextNode_WrapLine](GUITextNode_WrapLine.md)

## Notes

The name is ours (the IDB has sub_1403DDED8). The older text in GUITextNode_Draw said the horizontal 'auto' (4) becomes left 'unless the line ended on a forced break': the decompile says the flag is the soft-wrap flag set by sub_1403DE608, and then the line is justified (spaces for Latin, between glyphs for CJK); an unwrapped / last line is left aligned. Verified against live data for the single-line Job Tree nodes only.

## Open questions

? what sets st+88 other than sub_1403DE608 (no other writer was found in sub_1403DD3A0 or GUITextNode_PlaceGlyph). ? st+89 / st+90 meanings (read by GUITextNode_PlaceGlyph). ? the effect of the line flag (+20) and soft-wrap byte (+21) in GUITextNode_Draw (not read there per the earlier decode). ? multi-line behaviour was not checked against live memory (only a single-line node was read live).
