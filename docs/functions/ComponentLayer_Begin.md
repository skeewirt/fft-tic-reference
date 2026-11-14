# ComponentLayer_Begin

- **Address:** `0x1403E8FA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char ComponentLayer_Begin(UIRenderer *r, ComponentCtx *ctx, char force)`
- **Callers:** GUIComponentRef_Draw, sub_1403ED7D0
- **Callees:** ComponentEffects_Collect, sub_1403E647C, GUILayer_Select

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether a component needs its own offscreen layer and opens it.

## Behavior

- V: asks ComponentEffects_Collect (sub_1403E809C) whether any effect is enabled; the layer is also forced when r+606621 is set together with the target flags (ctx+488 +83, ctx+552, ctx+496 +561); returns 0 (no layer) when the context already carries one (ctx+553) or nothing needs it.
- V: when a layer is needed and ctx+409 is set without ctx+410 it marks ctx+410 and calls sub_1403E647C; then GUILayer_Select (sub_1403E9298) opens or reuses the layer and r+606588 / the record are updated.
- V (read 2026-10-30): the force rule in full: with the renderer feature byte r+606621 set (1 from the renderer initialiser), the layer is forced (a3 = 1) when widget byte +83 (ctx+488 + 83) is set and the context depth ctx+552 is 0 (the root component), or, otherwise, when the component byte +561 (ctx+496 + 561) is set. Layer opened = ctx+553 is 0 and (the effects collector returned 1 or the force applies). ctx+553 has no writer in the code (always 0), so a component inside a layer still opens its own layer when it has effects.
- V (live read): widget byte +83 is 1 for all 51 widgets of the running game, so every widget root opens a layer even with no effect enabled; the finger cursor's root component has no effect group and blend 0.

## State touched

- Calls: [ComponentEffects_Collect](ComponentEffects_Collect.md), [GUILayer_Select](GUILayer_Select.md)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Called by: [GUICore_DrawWidget](GUICore_DrawWidget.md), [GUINode_DrawKind10](GUINode_DrawKind10.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md), [WidgetRootsAreLayers](../behaviors/WidgetRootsAreLayers.md)

## Open questions

None recorded.
