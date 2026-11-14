# JobTree_SetArrowState

- **Address:** `0x1401347DC`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_SetArrowState(JobTreeAddon *addon, GUINode *lineNode, char onCursor, uint8_t met)`
- **Callers:** JobTree_OnCursorEnter, JobTree_OnCursorLeave
- **Callees:** UIName_Key, GUINode_FindState, GUINode_PlayState, GUINode_StopState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the look of one requirement arrow: activates exactly one of the named states Lock / Unlock / LockOnCursor / UnlockOnCursor on the line node.

## Behavior

- V: state index = met + (onCursor ? 2 : 0); the other three states are stopped (GUINode_StopState). Null node: no-op.
- V: 'met' = the required job is learned (record state == 0) and its level >= the edge's required level (see JobTree_OnCursorEnter).
- I: Lock = grey, Unlock = lit; the OnCursor pair is the highlighted variant drawn while the cursor is on either end of the arrow (green in game screenshots).

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobTree_OnCursorEnter](JobTree_OnCursorEnter.md), [JobTree_OnCursorLeave](JobTree_OnCursorLeave.md)
- Observed behaviours: [JobTreeLockState](../behaviors/JobTreeLockState.md)

## Notes

Arrows are `Line<A><B>` nodes authored in ffto_job_tree.uib; the states live in the shared shape component (LineBottom, LineRightBottom, ...).

## Open questions

None recorded.
