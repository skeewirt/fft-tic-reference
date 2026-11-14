# GUIComponent_TickTree

- **Address:** `0x140409284`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_TickTree(GUIComponent *comp, __int64 unused, char force)`
- **Callers:** GUIComponent_Update (sub_14040A1C8)
- **Callees:** GUIComponent_UpdateNodeTree, GUINode_ClearVisibleSubtree

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs GUIComponent_UpdateNodeTree on the component's root node (comp+272) when the component is active, else clears the visible flags once.

## Behavior

- V: when force != 0 or comp+559 != 0 or (comp+416 (loaded) != 0 and (comp+192 = 0 or comp+188 (opacity) > 0.0)): comp+562 = 1 and GUIComponent_UpdateNodeTree(comp, comp+272, force). Otherwise, if comp+562 was set, it is cleared and GUINode_ClearVisibleSubtree(comp, comp+272) runs once.

## State touched

- Calls: [GUIComponent_UpdateNodeTree](GUIComponent_UpdateNodeTree.md), [GUINode_ClearVisibleSubtree](GUINode_ClearVisibleSubtree.md)

## Referenced by

- Called by: [GUIComponentGauge_Update](GUIComponentGauge_Update.md), [GUIComponentScrollBar_Update](GUIComponentScrollBar_Update.md), [GUIComponent_Update](GUIComponent_Update.md)

## Notes

The name is ours (IDB: sub_140409284). Not in the task list (called by sub_14040A1C8); documented because it fixes what comp+272 and comp+562 are.

## Open questions

None recorded.
