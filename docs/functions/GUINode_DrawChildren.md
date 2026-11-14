# GUINode_DrawChildren

- **Address:** `0x1403E9A6C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_DrawChildren(UIRenderer *r, GUIContext *ctx, GUINode *layer)`
- **Callers:** GUIComponentRef_Draw (via sub_1403E9A2C), UI frame draw
- **Callees:** UIImageNode_Draw, GUITextNode_Draw, GUIComponentRef_Draw

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the children of a node in order, dispatching on each child's kind.

## Behavior

- V: skips the node when node+204 (visible) is 0 or node+145 (hidden) is set; starts at the first child (node+208), follows the +32 links to the LAST sibling and then steps backwards with +40, so the last entry of a node list is drawn first (bottom) and the first entry last (top); sets r+606596 = clamp(ctx+544 + child+200, -128, 127) + (r+606600 << 8) + 128 (the sort key).
- V: kind (child+52): 1 = recurse (this function), 2 = UIImageNode_Draw, 3 = GUITextNode_Draw, 4 = sub_1403EAF9C, 5 = sub_1403EBFA0, 6 = sub_1403EC4B0, 7 = sub_1403EC794, 8 = sub_1403ECA88, 10 = sub_1403ED7D0, 12 = GUIComponentRef_Draw, 14 = virtual draw (vtable +16).

## State touched

- Calls: [UIImageNode_Draw](UIImageNode_Draw.md), [GUITextNode_Draw](GUITextNode_Draw.md), [GUIComponentRef_Draw](GUIComponentRef_Draw.md)
- Reads: [GUINode.kind](../structs/GUINode.md#kind)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Called by: [GUIComponentRef_DrawChildren](GUIComponentRef_DrawChildren.md), [GUICore_DrawWidget](GUICore_DrawWidget.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md), [LayerCompositeOrder](../behaviors/LayerCompositeOrder.md)

## Open questions

Kinds 9, 11 and 13 are skipped here (?).
