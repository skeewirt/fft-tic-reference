# LayerShadow

- **Kind:** shader program
- **Area:** [Graphics](../areas/graphics.md)
- **Selector:** UI manager selector #10
- **Program index:** 1
- **Shaders:** [LayerQuadOffset_VS](../shaders/LayerQuadOffset_VS.md), [LayerShadow_PS](../shaders/LayerShadow_PS.md)
- **Applied by:** [GUILayer_BlurShadowPass](../functions/GUILayer_BlurShadowPass.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The drop-shadow draw: the layer quad moved by the offset, darkening the target under the blurred alpha.

## Behavior

- V (live read 2026-10-29): program 1 = shader objects 5 / 52 = VS 035438 / PS 035E50.
- V: the technique's default sampler words cover slots 13 and 16 only; slot 14 (g_Sampler, the shader's s0) keeps the default word.

## Referenced by

- Appears in flows: [LayerDropShadow](../flows/LayerDropShadow.md)
- Observed behaviours: [EffectPassesInheritDefaultSampler](../behaviors/EffectPassesInheritDefaultSampler.md)

## Open questions

None recorded.
