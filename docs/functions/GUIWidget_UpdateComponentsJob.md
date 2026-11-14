# GUIWidget_UpdateComponentsJob

- **Address:** `0x1403F94EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIWidget_UpdateComponentsJob(GUIWidget *w)`
- **Callers:** vtable entry (0x143D42100) and sub_14012B088, sub_14012B108, sub_1403D7A68
- **Callees:** GUINode_UpdateSubtree

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Work-stealing worker: updates the node tree of the widget's components in chunks of 16, so several threads can share one widget's component vector.

## Behavior

- V: n = (w+112 - w+104) / 8 (component vector at w+104..+112, pointers). While the shared counter w+600 < n: base = InterlockedExchangeAdd(w+600, 16); for i = base .. base+15 while i < n: comp = vec[i]; when comp+562 != 0 or comp+559 != 0, GUINode_UpdateSubtree(comp+272, comp+559 != 0).
- V: so +562 is the component's 'tree needs update' flag, +559 the 'force' flag (passed as the force argument).

## State touched

- Calls: [GUINode_UpdateSubtree](GUINode_UpdateSubtree.md)

## Notes

The name is ours (IDB: sub_1403F94EC). 15533 hits per 4 s. Each component is visited exactly once, in index order per chunk; the result of the per-node update does not depend on the thread, so a single-threaded simulator may just run it for i = 0..n-1.

## Open questions

? Who resets w+600 each frame (not in this function).
