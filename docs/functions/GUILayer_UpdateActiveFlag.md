# GUILayer_UpdateActiveFlag

- **Address:** `0x1403E6440`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUILayer_UpdateActiveFlag(UIRenderer *r, DrawCtx *ctx, char want)`
- **Callers:** GUINineGridNode_Draw, GUIRectNode_Draw, GUITextNode_Draw, UIImageNode_Draw, GUINode_DrawKind10, sub_1403EBFA0, sub_1403EC794, sub_1403ECA88 and a vtable entry
- **Callees:** GUILayer_Select

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the context's 'draws into an offscreen layer' byte (ctx+554) from a request and, when it changed, re-selects the layer.

## Behavior

- V: want is forced to 0 unless r+606626 != 0, ctx+412 != 0 and ctx+553 = 0. When ctx+554 != want: ctx+554 = want and the return value is GUILayer_Select(r, ctx); otherwise returns 0.

## State touched

- Calls: [GUILayer_Select](GUILayer_Select.md)

## Referenced by

- Called by: [GUINode_DrawKind5](GUINode_DrawKind5.md), [GUINode_DrawKind7](GUINode_DrawKind7.md), [GUINode_DrawKind8](GUINode_DrawKind8.md)

## Notes

The name is ours (IDB: sub_1403E6440). 6051 hits per 4 s. Every draw node calls it first, so most calls are a no-op compare.

## Open questions

? Meaning of ctx+412 (I: node has layer effects) and ctx+553 (I: forced flat / no layer).
