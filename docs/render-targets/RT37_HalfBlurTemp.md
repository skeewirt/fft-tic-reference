# RT37_HalfBlurTemp

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** RT 37
- **Size:** half output size (640 x 360 at 720p)
- **Format:** `R8G8B8A8_UNORM`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Half-size blur scratch: holds the horizontal pass of the half-size blur. Heads a second chain (RT 38..41).

## Behavior

- V (capture): the horizontal pass (sigma 2) of the 2 x 2 box downsample of RT26_LayerContent reproduces it to +-1 on 40 of 9600 values.

## Referenced by

- Appears in flows: [LayerGlowHalfSize](../flows/LayerGlowHalfSize.md)

## Open questions

None recorded.
