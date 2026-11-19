# InputGlyph_AppendId

- **Address:** `0x1400F3998`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void InputGlyph_AppendId(void *text, int id)`
- **Callers:** sub_1400F2648, sub_1400F39EC
- **Callees:** sub_1400798F8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends one glyph to a text buffer: the glyph escape code followed by the id with the high marker.

## Behavior

- V: appends glyph code 0xE104 followed by (id | 0xF0000) (through sub_1400798F8).

## Notes

Name is ours.

## Open questions

None recorded.
