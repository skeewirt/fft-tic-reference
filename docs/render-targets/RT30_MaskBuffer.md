# RT30_MaskBuffer

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** RT 30
- **Size:** output size
- **Format:** `R8_UNORM`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Mask buffer of masked layers: the mask pass reads its red channel.

## Behavior

- V: RT 30 is R8_UNORM at output size (live resource list); MaskComposite_PS reads mask.r.

## Referenced by

- Bound in shaders: [MaskComposite_PS](../shaders/MaskComposite_PS.md)

## Open questions

None recorded.
