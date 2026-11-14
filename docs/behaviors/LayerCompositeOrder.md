# LayerCompositeOrder

- **Kind:** observed behaviour
- **Scope:** the order of layers and of draws on the frame
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UIRender_PrepareLayers](../functions/UIRender_PrepareLayers.md), [GUINode_DrawChildren](../functions/GUINode_DrawChildren.md), [GUILayer_Select](../functions/GUILayer_Select.md), [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md), [LayerPassKeys](../registries/LayerPassKeys.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layers are composited in the order the game's draw traversal opened them, but only layers whose rectangles overlap are ordered against each other: each layer gets an order number that is one more than the creation index of the nearest overlapping lower layer, then the layers are sorted by (mode, order) and the order is renumbered densely. Within a layer the draws replay in the order they were recorded (children last-to-first, GUINode_DrawChildren).

## Behavior

- V: the list of used layers is built from the layer pointer table in index (creation) order; the layer's own order starts as its index.
- V: for every layer from the top of the list down, the nearest lower layer whose float rectangle (+208..+220) overlaps strictly (open intervals) sets order = that layer's current order + 1 (+ the page base); layers with no overlapping lower layer keep their index.
- V: the sort key then used is mode | (4 x order + 4) with mode = 1 for an ordinary layer (kind 0) with the drop-shadow or glow group, 2 for another ordinary layer, 0 for a whole-layer-blur layer; the orders are renumbered densely by key change. The sort comparator itself (sub_1403C2B00) was not read.
- V: the commands are executed by 64-bit key: target type, atlas page, pass (clear 1, draw 2, blit and effects 59), order; ties keep the recording order (stable merge sort in UIContext_SortCommands).
- V: GUINode_DrawChildren draws a node's children from the last entry to the first, so the first UIB entry is on top; a Reference node draws its whole component where it stands in the list.
- I: consequence for a renderer: composite the layers in creation order; layers that do not overlap can be done in any order; the pass order puts every layer's draws before any blit of the same atlas page and pages in ascending order.

## Referenced by

- Observed behaviours: [JobTreeLayerList](JobTreeLayerList.md)

## Open questions

? the exact comparator of the two sorts (equal keys) and whether a rectangle overlap test uses the effect margins (the rectangles are expanded by GUILayer_ExpandBounds before this runs).
