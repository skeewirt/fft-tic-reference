# RT3_EffectAlpha

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** RT 3
- **Size:** output size (1280 x 720 at 720p)
- **Format:** `R8G8B8A8_UNORM`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Effect alpha atlas: each layer with a drop shadow copies its alpha here (inside its atlas rectangle), the UI blur blurs it in place, and the shadow pass samples it. Reused during the frame: at frame end it no longer holds every layer's alpha.

## Behavior

- V (mid-frame capture 2026-10-30): before the name tag's shadow draw it held the blurred alpha of that layer and of the footer guides at their atlas places, plus other UI content.

## Referenced by

- Bound in shaders: [LayerShadow_PS](../shaders/LayerShadow_PS.md)

## Open questions

None recorded.
