# GUIComponentRef_DrawChildren

- **Address:** `0x1403E9A2C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponentRef_DrawChildren(UIRenderer *r, DrawCtx *ctx)`
- **Callers:** ComponentLayer_DrawMaskComponent, GUIComponentRef_Draw, GUINode_DrawKind10
- **Callees:** GUINode_DrawChildren

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the node tree of the component a reference node points at, or (when the layer mask path is active) just clears the current layer record's draw counter.

## Behavior

- V: when byte r+606628 != 0 or byte ctx+184 = 0 -> GUINode_DrawChildren(r, ctx, (ctx+496)->+272) (the component's root node).
- V: otherwise dword at r + 592 * (int r+606588) + 303508 = 0: field +28 of the current 592-byte layer record is zeroed and nothing is drawn.

## State touched

- Calls: [GUINode_DrawChildren](GUINode_DrawChildren.md)

## Notes

The name is ours (IDB: sub_1403E9A2C). 6401 hits per 4 s. ctx+496 is the component, +184 is a draw-enable byte, r+606588 is the current layer index (see GUILayer_SetCurrent).

## Open questions

? Meaning of r+606628 and of record field +28 (I: command count; the branch drops what the layer collected).
