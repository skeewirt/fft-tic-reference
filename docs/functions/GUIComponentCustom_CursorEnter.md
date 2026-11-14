# GUIComponentCustom_CursorEnter

- **Address:** `0x14040A20C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponentCustom_CursorEnter(GUINode *node)`
- **Callers:** GUICore_SetCursorTarget
- **Callees:** GUICore_GetFocus, GUINode_PlayCursorOverState, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Cursor-enter handler of a custom component (vtable slot +40): plays the CursorOver state and tells the node's owners.

## Behavior

- V: when the node is not the focus or its byte +574 is 0 it calls GUINode_PlayCursorOverState; then GUIOwners_PostEvent(node+584, node, {event 0x1407232F0}) posts the cursor-enter event to the owners (the job tree addon).

## State touched

- Calls: [GUICore_GetFocus](GUICore_GetFocus.md), [GUINode_PlayCursorOverState](GUINode_PlayCursorOverState.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Open questions

Event id value (?).
