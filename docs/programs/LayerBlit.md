# LayerBlit

- **Kind:** shader program
- **Area:** [Graphics](../areas/graphics.md)
- **Selector:** UI manager selector #9
- **Program index:** 0
- **Shaders:** [LayerBlendNormal_PS](../shaders/LayerBlendNormal_PS.md), [LayerBlendNormalOffsets_PS](../shaders/LayerBlendNormalOffsets_PS.md)
- **Applied by:** [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The layer blit: draws one layer's quad (rect - atlas offset) with the layer blend type as selector digit 0 and the offset-vector flag as digit 1. The pixel shader writes the frame target through a UAV; the fixed-function blend word GUILayer_BlitFinal stores (0x78020011: enabled, ONE / ZERO) therefore only matters when a shader writes a render target output.

## Behavior

- V: GUILayer_BlitFinal sets digit 0 = layer+32 (the blend type) and digit 1 = (any of the three offset vectors at layer+120.. is non-zero), applies program 0, then stores the blend word 2013397009 (0x78020011) at state+120 after the apply: enabled, source ONE, destination ZERO, add, alpha the same, write mask 0xF (decoded with the BlendDesc_FromWords field layout).
- V: the shaders of blend type 0 write no render-target output (their outputs list is empty); they write only UAV u0.

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Observed behaviours: [LayerBlitOverFrameTarget](../behaviors/LayerBlitOverFrameTarget.md)

## Open questions

? which of the 38 selector #9 programs a given blend type resolves to is inferred (see LayerBlendNormal_PS).
