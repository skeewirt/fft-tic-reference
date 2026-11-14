# RT32_HalfBlur

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** RT 32
- **Size:** half output size (640 x 360 at 720p)
- **Format:** `R8G8B8A8_UNORM`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Half-size blur target: first the 2 x 2 box downsample of the layer, finally the vertically blurred result. Heads a chain of smaller targets (RT 33..36: 320 x 180 down to 40 x 23).

## Behavior

- V (capture): the vertical pass (sigma = radius / 2) of RT37_HalfBlurTemp reproduces it to +-1 on 4 of 19200 values.

## Referenced by

- Appears in flows: [LayerGlowHalfSize](../flows/LayerGlowHalfSize.md), [LayerGlowHalfSize](../flows/LayerGlowHalfSize.md)

## Open questions

None recorded.
