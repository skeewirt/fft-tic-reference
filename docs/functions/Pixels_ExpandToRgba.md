# Pixels_ExpandToRgba

- **Address:** `0x14041DDB0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `uint64_t Pixels_ExpandToRgba(uint32_t *out, int64_t unused, uint8_t *src, uint32_t *palette, int w, int h, unsigned bpp, int outPitch)`
- **Callers:** HdLayer_BuildTextures, sub_140418F20, sub_14041E05C
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Expands a block of 4-, 8-, 16- or 32-bit pixels into 32-bit texels.

## Behavior

- V: bpp 4: two texels per byte, low nibble first, through the palette; with outPitch -1 the rows follow each other, else the output skips outPitch - w texels after each row.
- V: bpp 8: one texel per byte through the palette, rows following each other.
- V: bpp 16 (only with outPitch -1): each 5-5-5 word becomes a texel with each channel times 8 and the top byte all ones (the constant 0xFFFF8000 is shifted up with the blue channel).
- V: bpp 32: a plain copy of 4 * w * h bytes.

## Referenced by

- Called by: [HdLayer_BuildTextures](HdLayer_BuildTextures.md), [sub_14041E05C](sub_14041E05C.md)
- Observed behaviours: [SixteenColourLimitIsTwoCpuBuilders](../behaviors/SixteenColourLimitIsTwoCpuBuilders.md)

## Notes

The name is ours (IDB: sub_14041DDB0).

## Open questions

None recorded.
