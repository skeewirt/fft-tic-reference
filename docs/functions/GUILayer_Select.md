# GUILayer_Select

- **Address:** `0x1403E9298`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUILayer_Select(UIRenderer *r, ComponentCtx *ctx)`
- **Callers:** ComponentLayer_Begin, GUIComponentRef_Draw, sub_1403ED7D0
- **Callees:** GUILayer_Compatible, sub_1403E9218, GUILayer_BuildRecord, GUILayer_ResetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds an existing offscreen layer compatible with the context (same layer id and equal effect settings) or builds a new record, and makes it the current layer.

## Behavior

- V: searches layer records from the newest (index r+606584 - 1) down for one whose id (ctx+548) matches and for which GUILayer_Compatible (sub_1403E7ADC) holds; the result index (or -1) goes to sub_1403E9218 (makes it current, sets the per-thread draw target) and then GUILayer_BuildRecord (while the current layer index is below 510) or sub_1403E73A0 (reset the slot).

## State touched

- Calls: [GUILayer_Compatible](GUILayer_Compatible.md), [GUILayer_BuildRecord](GUILayer_BuildRecord.md), [GUILayer_ResetRecord](GUILayer_ResetRecord.md), [GUILayer_SetCurrent](GUILayer_SetCurrent.md)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Called by: [ComponentLayer_Begin](ComponentLayer_Begin.md), [GUILayer_UpdateActiveFlag](GUILayer_UpdateActiveFlag.md), [GUINode_DrawKind10](GUINode_DrawKind10.md), [GUINode_DrawKind8](GUINode_DrawKind8.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md), [LayerCompositeOrder](../behaviors/LayerCompositeOrder.md), [WidgetRootsAreLayers](../behaviors/WidgetRootsAreLayers.md)

## Notes

Layer records: 592 bytes at r + 303504 + 592 * i (512 slots, 510 usable).

## Open questions

None recorded.
