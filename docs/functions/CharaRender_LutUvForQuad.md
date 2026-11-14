# CharaRender_LutUvForQuad

- **Address:** `0x1400CBCE8`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void CharaRender_LutUvForQuad(__int64 unused, LutSlot *s, char a3, char a4, short rect[4], float uv[...])`
- **Callers:** CharaRender_DrawFrame, sub_14041AE44
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Computes the LUT texture coordinates at the four corners of a unit quad: the sprite is laid over a small region of the LUT sheet (width/height from CharShapeLUTParam) at the slot's LUT cell.

## Behavior

- V: inputs: rect = (left, top, right, bottom) as 16-bit classic px relative to the unit's ground point; region W = s+28 float x 64, H = s+32 float x 64; offsets P = short s+36, Q = short s+38; cell x = short s+8, y = short s+12 (pairs for a second LUT at s+16 / s+20).
- V: u = (P + x) / W clamped to [-0.9, 0.9] for left and right; v = -(Q + a4 + y) / H clamped to [-0.4, 1.4] for top and bottom.
- V: U = clamp01((u + 2 * cellX + 1) / 64), V = clamp01(1 - (v + 2 * cellY + 0.5) / 64), so a texel position is 128 * U, 128 * V in the 128 x 128 LUT sheet.
- V: corners (top-left, top-right, bottom-left, bottom-right) are written for LUT 1 and LUT 2 into interleaved float slots of the vertex scratch.

## Referenced by

- Called by: [CharaRender_DrawFrame](CharaRender_DrawFrame.md)

## Notes

The studio carries a software model of this (its lut_corner_uv routine). The rect argument is four 16-bit words (the decompiler shows ints).

## Open questions

None recorded.
