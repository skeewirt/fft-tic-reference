# JobScreen_UpdateState

- **Address:** `0x140368B4C`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `int64_t JobScreen_UpdateState(void)`
- **Callers:** no direct call sites (reached through a function table)
- **Callees:** JobListScreen_GetCursorIndex, JobList_IsSelectedEntryUnflagged, JobScreen_OpenJobPage, JobChange_RunPreviewAnim, JobScreen_RefreshAfterChange, JobTree_FillJobRecords, Unit_SpendJp, PartyUnit_WriteBackToSave, UnitWork_BuildFromSaveIndex, Unit_BuildPreviewSpriteRecord, Unit_ResolvePreviewShape, sub_1402888E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame state machine of the job screen (states 1400..1412): reads the job-change list cursor, picks the job from g_RuntimeJobList, shows its ability page, runs the job change and the preview animation.

## Behavior

- V: reads and writes g_JobListSelectedEntry (6 references in total: three writes in this function, reads here and in JobList_IsSelectedEntryUnflagged).
- V: calls JobListScreen_GetCursorIndex (4 sites), JobList_IsSelectedEntryUnflagged, JobScreen_OpenJobPage (0x140368D4A, 0x140368E85), JobChange_RunPreviewAnim (0x140368DC1), the job-change action sub_1402888E8, Unit_SpendJp, JobTree_FillJobRecords and JobScreen_RefreshAfterChange.
- V: three inline copies of the cursor-to-entry read exist: the load of the dword at +0x4A48 of the object pointed to by the qword at +0x78 of the screen object, at 0x140368FDE (states 1401 and 1405), the mouse click copy at 0x140368C40 (state 1408, from a2[1]) and the write at 0x140368E74 (state 1404).
- I: the name and the per-state meaning are inferred from the call pattern; the state numbers themselves are read from the code.
- V: the preview shape of the selected Change Job entry is Unit_ResolvePreviewShape(unit, .., the entry's low byte), zero-extended into edx at 0x140368FAC.

## State touched

- Calls: [JobListScreen_GetCursorIndex](JobListScreen_GetCursorIndex.md), [JobList_IsSelectedEntryUnflagged](JobList_IsSelectedEntryUnflagged.md), [JobScreen_OpenJobPage](JobScreen_OpenJobPage.md), [JobChange_RunPreviewAnim](JobChange_RunPreviewAnim.md), [JobScreen_RefreshAfterChange](JobScreen_RefreshAfterChange.md), [JobTree_FillJobRecords](JobTree_FillJobRecords.md), [Unit_SpendJp](Unit_SpendJp.md), [PartyUnit_WriteBackToSave](PartyUnit_WriteBackToSave.md), [Unit_BuildPreviewSpriteRecord](Unit_BuildPreviewSpriteRecord.md), [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md), [sub_1402888E8](sub_1402888E8.md)
- Reads: [JobRecord.jobId](../structs/JobRecord.md#jobid), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_JobListSelectedEntry](../globals/g_JobListSelectedEntry.md), [g_PartyUnits](../globals/g_PartyUnits.md), [g_RuntimeJobList](../globals/g_RuntimeJobList.md)
- Writes: [g_JobListSelectedEntry](../globals/g_JobListSelectedEntry.md)

## Referenced by

- Appears in flows: [JobScreenFrame](../flows/JobScreenFrame.md), [JobScreenFrame](../flows/JobScreenFrame.md)
- Observed behaviours: [JobListEntryWordMeaning](../behaviors/JobListEntryWordMeaning.md), [RuntimeJobListCanLiveInAnyBlockWithinReach](../behaviors/RuntimeJobListCanLiveInAnyBlockWithinReach.md), [RuntimeJobListIs48WordsFollowedByAnotherGlobal](../behaviors/RuntimeJobListIs48WordsFollowedByAnotherGlobal.md)

## Notes

Earlier notes called it JobList_StateMachine; one name is kept. It reads g_RuntimeJobList six times as image base + list RVA + index * 2 (rsi holds the image base from a rip-relative lea): at 0x140368D06 and 0x140368D42 the index is g_JobListSelectedEntry, at 0x140368DB9, 0x140368E7D, 0x140368EC5 and 0x140368F9A it is the result of the cursor call just before (JobListScreen_GetCursorIndex, wrapped by the scroll runtime); the read at 0x140368F9A takes only the low byte.

## Open questions

Full state table (only the cursor-reading states were read).
