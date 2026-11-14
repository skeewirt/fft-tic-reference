# GUIComponent_OnDown

- **Address:** `0x14040A324`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_OnDown(GUIComponent *comp)`
- **Callers:** vtable slot +56 (GUICore_UpdateFrame)
- **Callees:** GUINode_StopState, GUINode_FindState, GUINode_PlayState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Component virtual +56: the confirm button / mouse button went down on the component; sets the pressed flag, plays the Down state and posts event 14.

## Behavior

- V: comp+555 = 1; GUINode_StopState(comp, key +4728 = 'Up'); state = FindState(comp, key +4744 = 'Down'), +104 = 1, PlayState; event {14} to the owners.
- V (caller): GUICore_UpdateFrame calls virtual +56 on the pressed component (v29) when its +554 (enabled) is set (and, when +570 is set, only if it is the cursor target); otherwise it calls virtual +80 (the disabled-click response, not read).

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours (IDB: sub_14040A324); Down / Up / Click is the naming of the three state keys. Event 14 was listed only as '14..17' in the owner event notes.

## Open questions

? exactly which raw input (mouse left, confirm key) drives the press edge (GUICore_UpdateFrame reads cursor-state bytes +1903 / +1905).
