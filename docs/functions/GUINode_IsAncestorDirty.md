# GUINode_IsAncestorDirty

- **Address:** `0x1403EF834`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUINode_IsAncestorDirty(GUINode *node)`
- **Callers:** GUINode_UpdateSubtree, GUIComponent_UpdateNodeTree, sub_1403F1234 (text relayout)
- **Callees:** itself

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when the node or any ancestor has its dirty byte (+149) set.

## Behavior

- V: node+149 != 0, or (parent node+24 != 0 and the same test recursively on the parent).

## Referenced by

- Called by: [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_UpdateNodeTree](GUIComponent_UpdateNodeTree.md), [GUITextNode_UpdateLayout](GUITextNode_UpdateLayout.md)

## Notes

The name is ours (IDB: sub_1403EF834). Thunk-sized; listed because it gates text relayout.

## Open questions

None recorded.
