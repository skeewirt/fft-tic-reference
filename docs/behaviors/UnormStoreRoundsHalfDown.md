# UnormStoreRoundsHalfDown

- **Kind:** observed behaviour
- **Scope:** GPU (the test machine's GPU and driver)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [LayerShadow_PS](../shaders/LayerShadow_PS.md), [RT27_GlowBlurred](../render-targets/RT27_GlowBlurred.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

When a shader stores a float into an 8-bit UNORM target, an exact half rounds down: 16.5 stores 16, 9.5 stores 9.

## Behavior

- V (mid-frame capture 2026-10-30): 787 values of the name tag's shadow draw sit exactly on a half; all of them store the lower value, and with this rule every changed value of the four shadow draws is reproduced. D3D allows implementations to differ here, so other GPUs may round these values up.
- V (second capture, the ring glow's bilinear upscale): rounding halves down gives 0 differences of 27744 values; rounding them up gives 1384.

## Open questions

None recorded.
