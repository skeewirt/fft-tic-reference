# GUICore_DrawWidget

- **Address:** `0x1403E97A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_DrawWidget(UIRenderer *r, GUILayerXform *layer, GUIWidget *w)`
- **Callers:** GUICore_CommitFrame (widgets with +74 or +75 set and +79 clear, called with layer = core + 216 + 144 * int16 w+60)
- **Callees:** sub_1403DFE34, sub_1403F9D6C, sub_1403F8A20, ComponentLayer_Begin, GUINode_DrawChildren, sub_1403E9218, GUILayer_ResetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one widget: bumps the sort group when the widget's draw order word changes, fills the widget background, then builds the root draw context from the layer transform and draws the widget's main component tree.

## Behavior

- V: a = int16 w+62; when r+606616 != a: ++r+606600 and r+606616 = a. (r+606600 << 8 is the high part of every sort key, see GUINode_DrawChildren.)
- V: when the high byte of the dword w+64 is non-zero (background alpha) a flat quad (sub_1403DFE34) covering (0, 0, layer+24, layer+28) in the identity matrix (xmmword_140906D60 = 1,0,0,1) with colour w+64 and the sort key r+606596 is queued; ++r+606592.
- V: main component = sub_1403F9D6C(w) (first entry of the vector w+104..+112 with +536 == 1). It is drawn only when it exists, comp+416 (enabled) != 0 and (comp+192 == 0 or the float comp+188 > 0).
- V (root draw context, 0x258 bytes on the stack, zero-filled except): ctx+488 = w, ctx+496 = comp, ctx+504..+527 = the layer's matrix (layer+48..+71; recomputed first by sub_1403F8A20 when layer+128 is set), ctx+528 / +532 = layer+120 / +124 (the layer scale), ctx+536 = 0 (opacity add), ctx+540 = -1 (white), ctx+544 = 0 (order), ctx+548 = comp+552 << 16 (layer id), ctx+552 = 0 (depth), ctx+4 = 1.0f, ctx+132 / +148 / +476 = -1.
- V: opened = ComponentLayer_Begin(r, ctx, 0); when r+606628 != 0 or the layer flag the call set is clear, GUINode_DrawChildren(r, ctx, comp + 272) draws the component's root layer node; otherwise the field at r + 592*r[606588] + 303508 is zeroed instead. When a layer was opened: sub_1403E9218(r, -1) and GUILayer_ResetRecord(r, r[606588]) close it.
- V (live read 2026-10-30 + ComponentLayer_Begin): ComponentLayer_Begin is called at depth 0 with the root context, where the force rule applies: widget byte +83 is 1 for all 51 widgets, so the widget root always opens a layer (feature byte r+606621 = 1).

## State touched

- Calls: [ComponentLayer_Begin](ComponentLayer_Begin.md), [GUINode_DrawChildren](GUINode_DrawChildren.md), [GUILayer_ResetRecord](GUILayer_ResetRecord.md), [GUILayer_SetCurrent](GUILayer_SetCurrent.md)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md), [WidgetRootsAreLayers](../behaviors/WidgetRootsAreLayers.md)

## Notes

The name is ours (IDB: sub_1403E97A8). This is where a screen's draw starts: the root context has identity opacity (add 0), white colour and the window-to-UI matrix; every colour / opacity / order on the Job Tree page accumulates from here down through GUINode_DrawChildren and the component contexts.

## Open questions

? The meaning of ctx+4 = 1.0f and of the three -1 fields; what r+606628 is.
