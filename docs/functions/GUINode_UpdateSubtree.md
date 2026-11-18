# GUINode_UpdateSubtree

- **Address:** `0x1403F08C0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUINode_UpdateSubtree(GUINode *node, char force)`
- **Callers:** component / screen update code (sub_1400F56D8, GuideBar_LayoutRow, sub_1401AA85B, sub_1401F36A0, ... about 12 callers), itself
- **Callees:** GUINode_UpdateColourAndMatrix, sub_1403EF834 (any ancestor dirty), sub_1403F1FAC, sub_1403F2208

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recursive per-frame colour / matrix pass over a node and its children (siblings via +32), run before the component tree pass; also rebuilds the text-board nodes (kind 8) that changed.

## Behavior

- V: dirty = node+149; GUINode_UpdateColourAndMatrix(node, force). For each child (first child node+208, next +32): when dirty, child+149 = 1 (a dirty parent dirties every child, so a moved parent re-derives every child matrix).
- V: child kind 1 recurses; kind 8 runs GUINode_UpdateColourAndMatrix and, when the child is visible and (an ancestor chain is dirty (sub_1403EF834) or +279 is set or (+280 = 1 and +284 > 0.0 and +296 > 0.0)), clears +279 and runs sub_1403F1FAC then sub_1403F2208 (kind 8 geometry rebuild, not read); kind 14 calls its virtual method +8; every other kind just runs GUINode_UpdateColourAndMatrix.
- I: kind 8 is the kind that carries glyph-array style content (its fields +216..+224 are a vector of 552-byte elements, see GUINode_ApplyAnimChannels); kind 3 (text) is not rebuilt here, it is rebuilt in GUIComponent_UpdateNodeTree.

## State touched

- Calls: [GUINode_UpdateColourAndMatrix](GUINode_UpdateColourAndMatrix.md)
- Reads: [GUINode.kind](../structs/GUINode.md#kind)

## Referenced by

- Called by: [GUIWidget_UpdateComponentsJob](GUIWidget_UpdateComponentsJob.md), [GuideBar_LayoutRow](GuideBar_LayoutRow.md), [sub_14013DD70](sub_14013DD70.md)

## Notes

The name is ours (IDB: sub_1403F08C0). Kind 12 / 9 (component references) are not special-cased here: they take the generic branch, their inner trees are updated by their own component.

## Open questions

What kind 8 is (the +279 flag, +280 mode, +284 / +296 floats); what sub_1403F1FAC / sub_1403F2208 build.
