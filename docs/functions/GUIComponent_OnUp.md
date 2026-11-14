# GUIComponent_OnUp

- **Address:** `0x14040A3B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_OnUp(GUIComponent *comp)`
- **Callers:** vtable slot +64 (GUICore_UpdateFrame calls it as virtual +64)
- **Callees:** GUINode_StopState, GUINode_FindState, GUINode_PlayState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Component virtual +64: the press ended; clears the pressed flag, plays the Up state and posts event 15.

## Behavior

- V: comp+555 = 0; StopState(comp, key +4744 = 'Down'); FindState(comp, key +4728 = 'Up'), +104 = 1, PlayState; event {15} to the owners.

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours (IDB: sub_14040A3B4). Inverse of GUIComponent_OnDown.

## Open questions

None recorded.
