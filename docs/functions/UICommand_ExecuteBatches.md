# UICommand_ExecuteBatches

- **Address:** `0x1403C1004`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UICommand_ExecuteBatches(UIRenderer *r)`
- **Callers:** UI frame submit
- **Callees:** UIRender_FlushBatch, UIDrawState_Copy, sub_1403B0838

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Walks the frame sorted command list and draws it in batches, flushing a batch whenever the pipeline/state key changes.

## Behavior

- V: a batch breaks when the type nibble (&0xF0), the layer id, state words +8/+12 (&0x7FFFFFFF), the 0x1FF field, or any of the floats at +36/+40/+44 (0.5/0.2/1.0 defaults) differ from the previous command, or the vertex range is not contiguous; then UIRender_FlushBatch is called for the finished range.
- V: also selects the render-target dependent bits (scissor rectangle from the context at +208..+220) when the layer id changes.
- V (read 2026-10-30): each command carries a layer index; a layer that is culled (+79) or has no constants (+572 clear) is skipped. When the layer changes the function sets the sort key ((order & 0x1FF | ((page & 0x3F | target type << 18) << 15) | 0x6AC00400) << 10, pass 2), the draw target = the entry at g_Renderer + 800 x (byte target + 86) + 23720 (row slot 0, RT 26's resource: the layer content target), the target's format bits into state+124 bits 9..11, the scissor rectangle state+80 = {(int)x, (int)y, (int)(x + w), (int)(y + h)} of the layer's packed float rectangle (+208..+220, atlas coordinates), and binds the layer's constant buffer (layer+40) at the cUIRender slot (UI ring +66).
- V: the blend word is not set here: UIRender_FlushBatch -> UIRender_ApplyDrawState sets state+120 = the draw state's first dword (0x79420a11 in the default state: ONE / INV_SRC_ALPHA).

## State touched

- Calls: [UIRender_FlushBatch](UIRender_FlushBatch.md), [UIDrawState_Copy](UIDrawState_Copy.md), [UILayer_GetTarget](UILayer_GetTarget.md)
- Reads: [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [GUILayer.rect](../structs/GUILayer.md#rect), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [UIRender.slot_cUIRender](../structs/UIRender.md#slot_cuirender), [g_Renderer](../globals/g_Renderer.md), [GUILayer.used](../structs/GUILayer.md#used), [GUILayer.culled](../structs/GUILayer.md#culled)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.state_flags](../structs/RenderContext.md#state_flags), [RenderContext.cbuffer_handles](../structs/RenderContext.md#cbuffer_handles), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Called by: [UICommandRing_Flush](UICommandRing_Flush.md)
- Observed behaviours: [LayerContentDrawnIntoCleared8BitTarget](../behaviors/LayerContentDrawnIntoCleared8BitTarget.md)

## Open questions

Only the head of the function was read; the index building at its end is not documented (?).
