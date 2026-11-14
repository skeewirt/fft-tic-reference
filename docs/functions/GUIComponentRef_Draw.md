# GUIComponentRef_Draw

- **Address:** `0x1403EDB20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponentRef_Draw(UIRenderer *r, GUIContext *ctx, GUINode *ref)`
- **Callers:** GUINode_DrawChildren (kind 12)
- **Callees:** ComponentDrawContext_Build, ComponentEffects_Collect, sub_1403E8FA4, sub_1403E9A2C, sub_1403E9298

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a component reference node: finds the component, builds a draw context from its property block, opens an offscreen layer when the component has effects, draws its children, then composites the layer.

## Behavior

- V: component = sub_1403F9938(ctx+488, ref+208, ref+224, ref+304); skipped when it is absent, when component+416 is 0, or when component+192 is set and the opacity float component+188 is <= 0.
- V: ComponentDrawContext_Build copies the parent context (0x258 bytes) and multiplies matrix, opacity, colour and sort order; sub_1403E8FA4 decides whether an offscreen layer is needed (any effect group enabled) and opens it; sub_1403E9A2C draws the component children; sub_1403E9298 closes and composites the layer when one was opened.
- V (read 2026-10-30): the call is ComponentLayer_Begin(r, child context, 0) (no force); after the children, when a layer was opened, the parent's layer id (a2+548) is incremented when non-zero and GUILayer_Select(r, parent context) runs: the parent's later draws go to a NEW layer record built from the parent's context (an existing one is reused only when its id and settings match), so a child layer is bracketed by two records of the parent and keeps its place in the order. When no layer was opened the parent's offscreen flag ctx+554 is taken from the child's.
- V (live 2026-10-30, 26 slots of a Job Tree frame): the sequence of layer slots is reproduced exactly by this rule: a component that opens a layer takes the next slot, and the parent continues in the slot after it with the PARENT context (the continuation record carries the parent's inherited effect groups; the child context is a copy of the parent's, so effect groups inherited from ancestors stay set in nested contexts); a slot without any draw is reused, so only components with draws after them produce a continuation slot. See the behavior JobTreeLayerList.

## State touched

- Calls: [ComponentDrawContext_Build](ComponentDrawContext_Build.md), [ComponentEffects_Collect](ComponentEffects_Collect.md)

## Referenced by

- Called by: [GUINode_DrawChildren](GUINode_DrawChildren.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md), [WidgetRootsAreLayers](../behaviors/WidgetRootsAreLayers.md)

## Notes

The Job Tree hover ring is the component UnitSelect drawn through this path.

## Open questions

Layer composite shader selection (sub_1403E6728 / sub_1403E73A0) not yet decoded (?).
