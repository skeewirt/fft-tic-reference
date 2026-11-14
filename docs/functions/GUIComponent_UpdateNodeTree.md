# GUIComponent_UpdateNodeTree

- **Address:** `0x1404092EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIComponent_UpdateNodeTree(GUIComponent *comp, __int64 unused, GUINode *node, char force)`
- **Callers:** GUIComponent_TickTree (sub_140409284), itself, a handful of screen code paths (sub_1400F56D8, sub_14012D25C, ...)
- **Callees:** GUINode_ClearVisibleSubtree, GUINode_IsAncestorDirty, GUINode_ResolvePins_Fraction, GUINode_ResolvePins_Offset, GUIWidget_FindComponentCached, sub_1403F1234, sub_1403F2BD4, sub_1403F2EF8, sub_1403EF6B4, component virtual +32

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recursive layout / update walk over a component's node tree (started at comp+272 by sub_140409284): re-sorts layers by sort order, queues or runs the text relayout for dirty text nodes, and calls the update method of every nested component (kinds 9 and 12).

## Behavior

- V (cull): when force = 0 and comp+559 = 0 and (node+144 = 0 or node+108 <= 0.0 or (node+96 = 0 and the alpha byte node+103 of its own colour = 0)), the node and its whole subtree are skipped after GUINode_ClearVisibleSubtree (visible bytes +204 cleared). So a node with opacity <= 0, disabled, or an own colour of alpha 0 (with no colour id) is neither updated nor drawn, and neither are its children.
- V: otherwise sub_1403EF860 resolves the node's pin layout when node+140 is set (+141 = 0 -> GUINode_ResolvePins_Fraction, 1 -> GUINode_ResolvePins_Offset), then switch on kind (node+52):
- V: kind 1 (layer): when the re-sort flag node+216 is set, the child list (head node+208, next +32, previous +40) is insertion-sorted ascending by the children's sort order (+92) (stable: a later sibling moves ahead of an earlier one only when strictly smaller), flag cleared; then every child is processed recursively with the same force flag.
- V: kind 3 (text): when an ancestor is dirty (GUINode_IsAncestorDirty) or node+316 (text dirty) is set: if the widget's flag (comp+496 -> +84) is set the node is appended as a 16-byte record {0, node} to the widget's vector at +304 (deferred relayout), otherwise sub_1403F1234 (resolve text id +248, copy string, GUITextNode_Layout) runs at once.
- V: kind 9 (component reference with a 'mask' name at +248): component = GUIWidget_FindComponentCached(widget, node+248, node+264, node+288); none = return. The component's allocated size is set from the node's size (node+64/+68): comp+528 = width, comp+532 = height, swapped when comp+536 = 7 and comp+664 = 0; when comp+540 = 2 the component root is also resized to that size (sub_1403EF6B4(comp+272, ..)). Then the component's virtual method +32 is called (comp, time slot, changed = force or comp+559).
- V: kind 12 (component reference, name at +208): same lookup (node+208, +224, +304); node+303 set -> sub_1403F2BD4(node, comp, 0); then sub_1403F2EF8(node, comp) (copy the reference's overrides onto the component) and the same virtual +32 call. Other kinds do nothing.

## State touched

- Calls: [GUINode_ClearVisibleSubtree](GUINode_ClearVisibleSubtree.md), [GUINode_IsAncestorDirty](GUINode_IsAncestorDirty.md), [GUINode_ResolvePins_Fraction](GUINode_ResolvePins_Fraction.md), [GUINode_ResolvePins_Offset](GUINode_ResolvePins_Offset.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md)

## Referenced by

- Called by: [GUIComponent_TickTree](GUIComponent_TickTree.md), [ScrollHelper_Bind](ScrollHelper_Bind.md)

## Notes

The name is ours (IDB: sub_1404092EC). The cull in the first block is the only place found so far where an own colour alpha of 0 removes a subtree; it matters for the Job Tree because the TextMask rectangle and similar nodes are authored with colour data.

## Open questions

The semantics of the +559 flag (force-visible?) and of the deferred relayout queue; what sub_1403F2EF8 copies.
