# GUIComponent_Update

- **Address:** `0x14040A1C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_Update(GUIComponent *comp, float time, char force)`
- **Callers:** GUITextBoardComponent_Update, other component classes
- **Callees:** sub_1404099F4, GUIComponent_ApplyStateAnims, GUIComponent_TickTree

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Base per-frame update of a component: advance the state timers, apply the state animations, then update the node tree.

## Behavior

- V: sub_1404099F4(comp, time) (advance / stop the active states), GUIComponent_ApplyStateAnims(comp), GUIComponent_TickTree(comp, force).

## State touched

- Calls: [GUIComponent_ApplyStateAnims](GUIComponent_ApplyStateAnims.md), [GUIComponent_TickTree](GUIComponent_TickTree.md)

## Referenced by

- Called by: [GUITextBoardComponent_Update](GUITextBoardComponent_Update.md)

## Notes

The name is ours (IDB: sub_14040A1C8). Not in the task list.

## Open questions

None recorded.
