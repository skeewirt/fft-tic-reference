# Palette_ConvertToRgba

- **Address:** `0x14025EB10`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int Palette_ConvertToRgba(int kind, const short *src, unsigned int *dst)`
- **Callers:** sub_14025E984
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Converts a 16- or 256-colour palette of 15-bit words into 32-bit colours with alpha.

## Behavior

- V: the count comes from the palette format table (0x140672C38) by kind.
- V: word 0 becomes fully clear, 0x8000 opaque black; other words take their colour from a 32768-entry lookup.
- V: with semi-transparency on, words with the top bit take the alpha of the current blend mode (blend mode alpha table, 0x1407143E8), the others a fixed alpha; the return value says whether any opaque colour was seen.

## Referenced by

- Reads tables: [BlendModeAlpha](../tables/BlendModeAlpha.md), [PaletteFormats](../tables/PaletteFormats.md)

## Open questions

None recorded.
