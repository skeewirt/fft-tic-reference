# RT26_LayerContent

- **Kind:** render target
- **Area:** [Graphics](../areas/graphics.md)
- **Index:** RT 26
- **Size:** output size
- **Format:** `R8G8B8A8_UNORM`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layer content target: at the selection ring's glow pass it held the ring layer's own (sharp) pixels in its atlas place; the glow shader reads it as its second texture.

## Behavior

- V (mid-frame capture 2026-10-30, ring glow draw): the sharp ring (alpha up to 253) at atlas (66..135, 64..96); the glow composite reproduces the draw with this as B.
- V (live read 2026-10-30): the layer draw target (row 0 slot 0 of the per-type target table) and slot 26 of the per-type slot table share one resource pointer; it is the target of every layer's own UI draws (UICommand_ExecuteBatches), cleared to (0, 0, 0, 0) per atlas page (GUILayer_Composite), and the source of the layer blit (GUILayer_BlitFinal reads RT 26 first). See the flow UiLayerComposite.

## Referenced by

- Appears in flows: [LayerGlowHalfSize](../flows/LayerGlowHalfSize.md)
- Bound in shaders: [LayerBlendNormal_PS](../shaders/LayerBlendNormal_PS.md)
- Observed behaviours: [LayerContentDrawnIntoCleared8BitTarget](../behaviors/LayerContentDrawnIntoCleared8BitTarget.md)

## Open questions

None recorded.
