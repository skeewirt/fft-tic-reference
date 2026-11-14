# CursorDrawnThroughLayerTarget

- **Kind:** observed behaviour
- **Scope:** the finger cursor's glove (UI layer)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UIImage_PS](../shaders/UIImage_PS.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The glove reaches the screen in two 8-bit stores: it is drawn into a cleared layer target (premultiplied, rounded) and that layer is then blended onto the frame (dst = layer + dst * (1 - layer alpha), rounded again).

## Behavior

- V (glove captures, model comparison): one store reproduces 76.3 % of the glove's changed values (max 2), two stores 93.3 % (max 1) and with the 1/256 snapping and weights 99.4 %.
- V (2026-10-30, code): every widget root is a layer (WidgetRootsAreLayers), so the glove, which has no effect of its own, goes through the layer path like all other UI: its draws land in RT 26 (cleared to (0, 0, 0, 0) per atlas page, blend ONE / INV_SRC_ALPHA) and the layer is then composited onto the frame target by a shader read-modify-write (LayerBlitOverFrameTarget). The general rule and its order are in the flow UiLayerComposite and the behavior LayerCompositeOrder.
- V: the formulas are in LayerContentDrawnIntoCleared8BitTarget (store 1) and LayerBlitOverFrameTarget (store 2).

## Open questions

? the order of the layers on the Job Tree screen itself was not read live (only a screen that was running when this was decoded); the order rule is in LayerCompositeOrder.
