# JobChangeAddon_SetState

- **Address:** `0x14012FC6C`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobChangeAddon_SetState(JobListAddon *addon, int state, bool force)`
- **Callers:** JobList_SelectEntry, sub_14012E620, sub_14012E640, sub_14012E82C, sub_140130DF0, sub_140131068, sub_1401312C8
- **Callees:** JobList_OnCursorChanged, TabBar_Select, TabBar_SetTable, GUICore_FocusNode, GUIComponent_Enable, GUIComponent_Disable, JobTable_GetRow, UITable_GetRowByKey, CharaRender_SetSlotRequest

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Switches the job-change list addon (UIAddonFFTOUnitJobChange2) to a new mode and updates focus, tab bar, sprite requests and cursor for that mode.

## Behavior

- V: the mode lives at addon+19008; returns at once when the new state equals it and force is 0.
- V: leaving mode 2 calls sub_1401332A0(addon, 0); the mode is then stored and a switch (modes 2..10 and more) sets up each mode.
- V: calls JobList_OnCursorChanged at 0x1303A7, plus TabBar_Select/SetTable, GUICore_FocusNode, GUIComponent_Enable/Disable, JobTable_GetRow and CharaRender_SetSlotRequest.
- V: 7 callers, including JobList_SelectEntry (modes 6 and 3).

## State touched

- Calls: [JobList_OnCursorChanged](JobList_OnCursorChanged.md), [TabBar_Select](TabBar_Select.md), [TabBar_SetTable](TabBar_SetTable.md), [GUICore_FocusNode](GUICore_FocusNode.md), [GUIComponent_Enable](GUIComponent_Enable.md), [GUIComponent_Disable](GUIComponent_Disable.md), [JobTable_GetRow](JobTable_GetRow.md), [UITable_GetRowByKey](UITable_GetRowByKey.md), [CharaRender_SetSlotRequest](CharaRender_SetSlotRequest.md)
- Reads: [JobRecord.jobId](../structs/JobRecord.md#jobid), [JobRecord.state](../structs/JobRecord.md#state), [JobRecord.showUse](../structs/JobRecord.md#showuse), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Referenced by

- Called by: [JobList_SelectEntry](JobList_SelectEntry.md)

## Notes

Mode meanings: 2 browsing, 3 and 6 chosen by JobList_SelectEntry, 9 ability page; others not mapped.

## Open questions

Per-mode behaviour.
