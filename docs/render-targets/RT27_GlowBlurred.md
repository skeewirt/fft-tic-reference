# RT27_GlowBlurred

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** RT 27
- **Size:** output size
- **Format:** `R8G8B8A8_UNORM`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Full-resolution blurred layer read by the glow pass (its first texture); for a half-size blur it is the bilinear upscale of RT32_HalfBlur.

## Behavior

- V (capture): equals the bilinear upscale of RT 32 (pixel centre x / 2 - 0.25 in half-size texels) with 8-bit stores rounding halves down: 0 of 27744 values differ.

## Referenced by

- Appears in flows: [LayerGlowHalfSize](../flows/LayerGlowHalfSize.md)
- Observed behaviours: [UnormStoreRoundsHalfDown](../behaviors/UnormStoreRoundsHalfDown.md)

## Open questions

None recorded.
