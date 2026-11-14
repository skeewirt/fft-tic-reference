# GUIComponent_OnFocusLost

- **Address:** `0x14040A5D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponent_OnFocusLost(GUINode *comp)`
- **Callers:** GUICore_SetFocusComponent
- **Callees:** GUINode_StopState, GUINode_FindState, GUINode_PlayState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Component virtual +104: plays FocusOut and posts event 20 (JobTree_OnCursorLeave).

## Behavior

- V: stops FocusIn (+4664), plays FocusOut (+4680), GUIOwners_PostEvent {20}. (The CursorOver / CursorOut states at +4696 / +4712 are played by the cursor enter / leave virtuals and by GUINode_SetCursorOverState; V: the UnitJob UIB has no FocusIn / FocusOut state, its hover look is CursorOver.)

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Open questions

None recorded.
