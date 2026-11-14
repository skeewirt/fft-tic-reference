# GUITextNode_PlaceGlyph

- **Address:** `0x1403DD780`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_PlaceGlyph(GUITextLayout *layout, GUITextLayoutState *st)`
- **Callers:** GUITextNode_Layout (one call per character not consumed by sub_1403DD3A0)
- **Callees:** sub_1400798F8 (UTF-8 encode), sub_1403A9A9C (glyph advance), sub_1403BF9D4 (UTF-8 decode), sub_1403A9114 (kerning pair), sub_1403A942C (shear width), sub_1401CBD68 (vector grow), sub_1403DE608 (word wrap)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Places one character of the string into the node's glyph vector: looks up its advance, applies fixed-width centring, italic and kerning adjustments, appends a 36-byte glyph record and advances the pen; wraps the line when the overflow mode is 0 and the glyph does not fit.

## Behavior

- V (arguments): layout (a1): glyph vector at +8 / +16 / +24 (begin / end / capacity, 36-byte records), line vector at +40 / +48 (24-byte), language flags +120..+124 (+123 = ja / zh). st (a2): +0 node, +36 pen x, +40 line y, +48 y shift (added to rec.y), +52 f (glyph multiplier: UIFontType UnknownC, or Unknown10), +56 x extra (see below), +60 the character (UTF-32 code), +64 glyphs already in this line, +67.. colour index stack indexed by byte +84, +86 bold counter, +87 italic counter, +89 a byte copied to rec+32, +90 soft-hyphen-suppress byte. Locals: W = (float)(int32 node+64), size = (float)(int16 node+304), R = the renderer (qword_143CDA098 + 37944).
- V (advance): lookup char = 32 for U+00A0, 45 for U+2011 and U+00AD (173), else the char; it is encoded as UTF-8 and sub_1403A9A9C returns (R+9500 * glyph +16, R+9504 * glyph +20) = scaled (advance, y-advance), the first is used: adv. If adv is ~0 (missing glyph) the char is replaced by U+25A0 (non-Japanese language) or U+3013 (Japanese), written back to st+60, and the lookup is repeated. If st+90 is set and the char is 173, adv = 0 and the x extra = 0.
- V (width): width = f * adv. If node+313 is set and not (node+315 set with a non-Japanese language): cell = f * size (size * 0.5 when the char is <= 0xFF), x offset = (cell - f * adv) * 0.5 and width = cell - x offset, so the glyph is centred in a fixed cell. I: node+313 is therefore a fixed-pitch (monospace) text flag; GUINode_BuildFromFile copies it from text block byte +78.
- V (x offset when the line already has a glyph): prev = last record of the glyph vector (the one before it when that record is a soft hyphen). x offset += st+56 (x extra: GUITextNode_Layout stores size * UIFontType.Unknown14 + int16 node+306 there, so it is a per-glyph spacing term). Italic transition (R+189 set): if shear R+9524 < 0 and prev is not italic (+29) and this glyph is italic: x offset -= S * f; if shear > 0 and prev is italic and this glyph is not: x offset += S * prev.f; S = sub_1403A942C (see GUITextNode_FinishLine). Kerning (only when not in fixed-width mode, or node+315 with a non-Japanese language, and R+189 set): the pair (prev char, this char) is looked up by sub_1403A9114 (binary search in the font's kerning table at font+216/+224 plus a second table at font+200); x offset += f * R+9500 * kern.x and the y offset = f * R+9500 * kern.y (zero otherwise).
- V (record appended, 36 bytes): +0 x = x offset + st+36 (pen), +4 y = y offset + st+48, +8 width, +12 f, +16 dword 0, +20 u16 char, +22 u16 ordinal of the glyph in the node, +24 u16 index of the line it belongs to (current line count), +26 byte colour index (st[67 + st+84], 0 when st+84 = 0), +27 0, +28 bold (st+86 != 0), +29 italic (st+87 != 0), +30 u16 0, +32 byte st+89. The vector grows through sub_1401CBD68 when full.
- V (pen): unless the char is 173, st+36 += x offset + width; st+64 += 1.
- V (wrap): when node+260 (overflow) is 0 and rec.x + width > W it returns sub_1403DE608(layout, st), the word wrap, which moves the glyphs after the last break opportunity to a new line (sets st+88 = 1 and calls GUITextNode_FinishLine for the finished part). Other overflow modes are handled in GUITextNode_FinishLine.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md), [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours (the IDB has sub_1403DD780). Hex-Rays lost the register for the st+56 and size locals in places; they were taken from the disassembly (movss xmm5 = [st+38h], xmm3 = int16 node+130h). The earlier text 'rec.width = advance * size/64' is consistent: R+9500 is size / 64 (GUITextNode_SetRenderScale).

## Open questions

? the exact meaning of st+89 / st+90 and of the colour index stack (+67..) was not traced (tag handler sub_1403DD3A0). ? whether the fallback glyph branch also updates the 'previous char' used for the soft-hyphen test (the decompile keeps the old copy). ? the second kerning table (font+200, sub_1403BA2D4) and the y-advance (R+9504 * glyph +20) were not decoded. ? the italic-transition rules were read as written; the intent (compensating the shear overhang) is I.
