# BlendDesc_FromWords

- **Address:** `0x140051284`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char BlendDesc_FromWords(_DWORD *desc, unsigned char count, unsigned char perTarget, unsigned int *words)`
- **Callers:** pipeline state creation
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Unpacks packed render-target blend words into the Direct3D 12 blend description array of a pipeline state.

## Behavior

- V: per target word w: BlendEnable = w & 1, BlendOp = ((w >> 1) & 7) + 1, SrcBlend = ((w >> 4) & 0x1F) + 1, DestBlend = ((w >> 9) & 0x1F) + 1, BlendOpAlpha = ((w >> 14) & 7) + 1, SrcBlendAlpha = ((w >> 17) & 0x1F) + 1, DestBlendAlpha = ((w >> 22) & 0x1F) + 1, RenderTargetWriteMask = (w >> 27) & 0xF; each target record is 40 bytes (10 dwords); the header holds the target count (a2) and independent-blend flag (a3 != 0 selects a per-target count).

## Notes

The packed words come from the draw state (state+0 for target 0) and from the program entries (+8...); the default UI draw state word0 is 0x79420a11 (ONE / INV_SRC_ALPHA).

## Open questions

None recorded.
