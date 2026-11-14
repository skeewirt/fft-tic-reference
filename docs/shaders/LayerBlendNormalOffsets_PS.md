# LayerBlendNormalOffsets_PS

- **Kind:** shader
- **Stage:** pixel
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x0080E8`
- **DXBC hash:** `2d12a4bf5565d31a56c786f480161219`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Blend type 0 with the offset variant (digit 1 = 1): the same over composite as LayerBlendNormal_PS with extra samples at the layer's three offset vectors (selected when any of them is non-zero).

## Behavior

- I: five samples instead of three, otherwise the same arithmetic as the offset-free shader (diff of the DXIL text of the pair 0x006E60 / 0x0080E8 not read line by line).

## Referenced by

- Used in programs: [LayerBlit](../programs/LayerBlit.md)

## Open questions

? the exact use of the three offset vectors (layer+120..+140).
