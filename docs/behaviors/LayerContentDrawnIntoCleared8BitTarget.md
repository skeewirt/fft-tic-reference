# LayerContentDrawnIntoCleared8BitTarget

- **Kind:** observed behaviour
- **Scope:** every layer's own draws
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UiLayerComposite](../flows/UiLayerComposite.md), [UICommand_ExecuteBatches](../functions/UICommand_ExecuteBatches.md), [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md), [RenderCommand_ClearTarget](../functions/RenderCommand_ClearTarget.md), [RT26_LayerContent](../render-targets/RT26_LayerContent.md), [UIImage_PS](../shaders/UIImage_PS.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Store 1: a layer's UI draws go into the layer content target (RT 26, RGBA8 UNORM, 1280 x 720) inside the layer's atlas rectangle, which starts cleared to (0, 0, 0, 0), with the fixed-function blend ONE / INV_SRC_ALPHA. The pixel shader's output is premultiplied, so the stored pixel is premultiplied colour and coverage alpha.

## Behavior

- V: the draw target is the object in row 0 slot 0 of the per-type target table (Renderer + 0x5CA8 + 800 x type) and its resource is the one of slot 26 of the per-type slot table (RT 26) (live read: the two views hold the same resource pointer).
- V: the blend word of an image draw is the draw state's first dword, set by UIRender_ApplyDrawState after the program apply; the default draw state (data at 0x1408FF878) holds 0x79420a11: blend on, SRC = ONE, DEST = INV_SRC_ALPHA, add, SRC_ALPHA = ONE, DEST_ALPHA = INV_SRC_ALPHA, add, write mask 0xF (fields decoded as BlendDesc_FromWords does: +1 on each 5-bit factor).
- V: clear: GUILayer_Composite queues a type-0 command per cleared target once per atlas page (dedupe through dword_140906B5C, reset each frame by UIRender_PrepareLayers); the command carries the target view and 16 zero bytes of colour; its executor is a ClearRenderTargetView call (D3D12 command list slot +384 = index 48) with that colour.
- V: the clear is per atlas page, not per layer: layers of a page occupy distinct rectangles (shelf allocator, margin 2 px) and the pass order puts the page's clear first.
- V: the scissor rectangle of the layer's draws is (int)x, (int)y, (int)(x + w), (int)(y + h) of the packed layer rectangle (atlas coordinates).
- I: formula for a renderer: for each image pixel p covered by a draw, in draw order, L(p) = clamp(S(p) + L(p) x (1 - S.a(p))) per channel with S the premultiplied shader output, L stored as unsigned-normalised 8 bits after every draw; the first draw into an empty pixel stores round8(S). The rounding of a blend result at the ROP (ties) was not captured separately (the 8-bit shader stores round halves down on the test GPU, see UnormStoreRoundsHalfDown).

## Open questions

? rounding of fixed-function blend results at exact ties.
