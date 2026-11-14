# JobTree_SetLabelState

- **Address:** `0x1401348B0`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_SetLabelState(JobTreeAddon *addon, GUINode *labelBoard, char show, char met)`
- **Callers:** JobTree_OnCursorEnter, JobTree_OnCursorLeave
- **Callees:** UIName_Key, GUINode_FindState, GUINode_PlayState, GUINode_StopState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets one level-label board: activates exactly one of the named states Hide / ShowLock / ShowUnlock.

## Behavior

- V: state = 0 (Hide) when !show; otherwise 1 (ShowLock) or 2 (ShowUnlock) by `met`. Others are stopped. Null board: no-op.
- I: ShowLock is the red 'not yet' chip, ShowUnlock the green one (as seen: green 'Lv. 4' chips).

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobTree_OnCursorEnter](JobTree_OnCursorEnter.md), [JobTree_OnCursorLeave](JobTree_OnCursorLeave.md)

## Notes

Boards are the `TextBoardJobLv{L,R,T,B}` children of the panel template (component UnitJob); one board is shared by every requirement that lands on that side of that panel.

## Open questions

None recorded.
