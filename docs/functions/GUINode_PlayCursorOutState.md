# GUINode_PlayCursorOutState

- **Address:** `0x14040A0E4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUINode_PlayCursorOutState(GUINode *node)`
- **Callers:** GUIComponent_CursorLeave, GUIComponent_OnFocusLost-family paths (GUIComponent_OnFocusLost itself plays FocusOut / CursorOut inline)
- **Callees:** GUINode_StopState, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stops the CursorOver state, starts the CursorOut state and clears the cursor-over flag +574 (mirror of GUINode_PlayCursorOverState).

## Behavior

- V: GUINode_StopState(node, key +4696 = 'CursorOver'); state = GUINode_FindState(node, key +4712 = 'CursorOut'); when it exists +104 = 1 and GUINode_PlayState; node+574 = 0.

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponent_CursorLeave](GUIComponent_CursorLeave.md)

## Notes

The name is ours (IDB: sub_14040A0E4). The key names are V from the static list (see the file docstring). Careful: the focus pair GUIComponent_OnFocusGained / OnFocusLost use the keys +4664 / +4680, which the same list names 'FocusIn' / 'FocusOut', not CursorOver / CursorOut as their sheets say; the CursorOver / CursorOut pair is only played by the cursor enter / leave virtuals.

## Open questions

None recorded.
