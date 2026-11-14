# GUIComponent_OnFocusGained

- **Address:** `0x14040A534`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIComponent_OnFocusGained(GUINode *comp)`
- **Callers:** GUICore_SetFocusComponent
- **Callees:** GUINode_StopState, GUINode_FindState, GUINode_PlayState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Component virtual +96: plays the component's FocusIn state (if the UIB has one; UnitJob has none, so nothing plays there) and posts event 19 to its owners.

## Behavior

- V: only when comp +416 (enabled) is set; stops the FocusOut state (UI name key at qword_143CDA2A0+4680; V: static name list at 0x1406F6100 index 6), plays the FocusIn state (+4664, index 5), then GUIOwners_PostEvent with the event template {19}.

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

JobTree_OnEvent case 0x13 -> JobTree_OnCursorEnter; this is where that event originates.

## Open questions

None recorded.
