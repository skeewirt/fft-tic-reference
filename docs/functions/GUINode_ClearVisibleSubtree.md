# GUINode_ClearVisibleSubtree

- **Address:** `0x1404095B8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_ClearVisibleSubtree(GUIComponent *comp, GUINode *node, ...)`
- **Callers:** GUIComponent_UpdateNodeTree (culled nodes), GUIComponent_TickTree, itself
- **Callees:** GUIWidget_FindComponentCached

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the visible byte (+204) to 0 for a node and everything below it, following layer children and nested components.

## Behavior

- V: loop on node: node+204 = 0; kind 1 recurses into every child (+208 / +32); kind 9 (name +248) and kind 12 (name +208) find the referenced component (GUIWidget_FindComponentCached) and continue with that component's root (comp+272); kind 9 sets the component's +562 = 1 first, kind 12 returns unless the component's +562 is set and then clears it. Other kinds stop after clearing their own flag.

## State touched

- Calls: [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md)
- Reads: [GUINode.kind](../structs/GUINode.md#kind)

## Referenced by

- Called by: [GUIComponent_TickTree](GUIComponent_TickTree.md), [GUIComponent_UpdateNodeTree](GUIComponent_UpdateNodeTree.md)

## Notes

The name is ours (IDB: sub_1404095B8). The renderer skips nodes with +204 = 0, so this is the 'hide' for culled subtrees.

## Open questions

Why kind 9 sets +562 and kind 12 clears it (looks like the mask component is kept alive so it can still be drawn into its layer).
