# InputGlyph_AppendPadButton

- **Address:** `0x1400F39EC`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void InputGlyph_AppendPadButton(void *text, uint32 binding, int alternate)`
- **Callers:** sub_1400F2648
- **Callees:** sub_1400F6C58, sub_1400F3998, sub_1400F3940, UITable_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the glyph text of an action's button into a text buffer: pad glyphs or keyboard modifier and key glyphs.

## Behavior

- V: pad mode (input module +13696 == 0): reads the UIPadDefine row of the pad button (the low 16 bits of the binding, taken with a zero-extending load): glyph (+4), or glyph_alt (+0xC) when the alternate flag is set and +0xC is non-zero; then, when glyph_2 (+8) is non-zero, a separator (sub_1400F3940) and glyph_2 follow.
- V: keyboard mode (+13696 == 1): the modifier glyphs for binding bits 18, 16 and 17 (flags 0x40000 Shift, 0x10000 Ctrl, 0x20000 Alt; tested as bit numbers, the masks are not in the body), then the key's glyph when UI table 35 has a row for it.
- V: the glyph text is written by InputGlyph_AppendId (sub_1400F3998), which owns the glyph escape code and the id marker.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md)

## Referenced by

- Observed behaviours: [KeyIconTag](../behaviors/KeyIconTag.md)

## Notes

Name is ours. Row +0 of UIPadDefine is never read.

## Open questions

None recorded.
