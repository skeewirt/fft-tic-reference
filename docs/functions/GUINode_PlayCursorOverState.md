# GUINode_PlayCursorOverState

- **Address:** `0x14040A094`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUINode_PlayCursorOverState(GUINode *node)`
- **Callers:** GUIComponentCustom_CursorEnter
- **Callees:** GUINode_StopState, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stops the node's CursorOut state, starts its CursorOver state and sets the cursor-over flag (+574).

## Behavior

- V: GUINode_StopState(node, key at qword_143CDA2A0+4712), GUINode_FindState(node, key at +4696) then +104 = 1 and GUINode_PlayState; byte node+574 = 1.

## State touched

- Calls: [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponentCustom_CursorEnter](GUIComponentCustom_CursorEnter.md)
- Observed behaviours: [JobTreeHoverFade](../behaviors/JobTreeHoverFade.md)

## Notes

The state keys are the UIName keys 'CursorOver' (+4696) and 'CursorOut' (+4712) (names read in the live state traces).

## Open questions

None recorded.
