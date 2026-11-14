# LayerAlphaCopy

- **Kind:** shader program
- **Area:** [Graphics](../areas/graphics.md)
- **Selector:** UI manager selector #10
- **Program index:** 0
- **Shaders:** [FullscreenTriangle_VS](../shaders/FullscreenTriangle_VS.md), [AlphaCopy_PS](../shaders/AlphaCopy_PS.md)
- **Applied by:** [GUILayer_CopyToTarget](../functions/GUILayer_CopyToTarget.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

First step of a layer's drop shadow: copies the layer alpha into RT3_EffectAlpha inside the layer's atlas rectangle.

## Behavior

- V (live read of the selector's program table, 2026-10-29): program 0 = shader objects of VS 034080 and PS 0349C0.

## Open questions

None recorded.
