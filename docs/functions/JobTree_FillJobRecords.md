# JobTree_FillJobRecords

- **Address:** `0x140368424`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_FillJobRecords(...)`
- **Callers:** addon vtable refresh path
- **Callees:** sub_14012EC5C, JobTree_SetPanelRecord, sub_1400FBB7C, sub_1402C1D40, Unit_ResolvePreviewShape

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Walks `g_RuntimeJobList` and, per list position, builds the 148-byte job record plus the sprite record, then hands them to the job-change list (sub_14012EC5C) and the tree (JobTree_SetPanelRecord).

## Behavior

- V: stock loop bound is min(19, g_RuntimeJobListLen): the 19 is a 32-bit immediate loaded into edx at 0x1403686E9.
- V: the stock list of a generic unit in mode 3 is 21 entries (74..93 without one of 91/92, then 160 and 161 flagged 0x2000), so positions 19 and 20 (the hidden extras) are never drawn by the stock bound.
- V: the sprite record's render slot (record +0x5C) is set to 61 + list position; the tree panels use slots 80 + panel, so a list position of 19 or more names a tree panel's slot.
- V: job id = word_143C51890[pos] & 0x3FF; calls sub_1400FBB7C (job row -> record), JobRecord_FillIconAndGenericFlag, sub_1402C1D40.
- V: record state at +132 (assigned from the runtime job-list entry): 2 = LockUnreleased when entry bit 0x2000 is set, or when a story flag (sub_1400FF8A4(unit, 2010)) is set and the job id is 78..93; 1 = LockReleased when bit 0x4000 is set; otherwise 0 (unlocked; +137 is then set when sub_1402867BC(...) reports 0). The current job is not a state: rec+141 (showUse) = the unit's job == this job.
- V: preview shape: for ids {160,161,164} or 74..93 uses an inline formula (`female + 2*job - 52` generic; 160 -> `female - 97` = 159/160; 161/164 -> `female - 95`), else Unit_ResolvePreviewShape. Special-case base constant is the immediate 0xA0 (160) loaded into a register at 0x14036898D.
- V: calls sub_14012EC5C(listAddon, record, pos) and JobTree_SetPanelRecord(treeAddon, record, pos).
- V: every shape branch of a cell joins at 0x140368A03, where dl is zero-extended into eax and stored as a dword into the record.

## State touched

- Calls: [JobTree_SetPanelRecord](JobTree_SetPanelRecord.md), [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md)
- Reads: [JobRecord.jobId](../structs/JobRecord.md#jobid), [JobRecord.state](../structs/JobRecord.md#state), [g_PartyUnits](../globals/g_PartyUnits.md), [g_RuntimeJobList](../globals/g_RuntimeJobList.md), [g_RuntimeJobListLen](../globals/g_RuntimeJobListLen.md), [JobListWord.job_id](../structs/JobListWord.md#job_id), [JobListWord.locked](../structs/JobListWord.md#locked), [JobListWord.current_job](../structs/JobListWord.md#current_job)
- Writes: [JobRecord.state](../structs/JobRecord.md#state), [JobRecord.showUse](../structs/JobRecord.md#showuse), [g_RuntimeJobListLen](../globals/g_RuntimeJobListLen.md)

## Referenced by

- Called by: [JobScreen_RefreshAfterChange](JobScreen_RefreshAfterChange.md), [JobScreen_UpdateState](JobScreen_UpdateState.md)
- Observed behaviours: [GenericUnitSpriteNumberFromJob](../behaviors/GenericUnitSpriteNumberFromJob.md), [JobListEntryWordMeaning](../behaviors/JobListEntryWordMeaning.md), [JobTreeLockState](../behaviors/JobTreeLockState.md), [JobTreePanelCountLimits](../behaviors/JobTreePanelCountLimits.md), [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md), [JobTreePanelSprite](../behaviors/JobTreePanelSprite.md), [LookSitesUseTheSaveRecordNotTheSlot](../behaviors/LookSitesUseTheSaveRecordNotTheSlot.md), [RuntimeJobListCanLiveInAnyBlockWithinReach](../behaviors/RuntimeJobListCanLiveInAnyBlockWithinReach.md), [RuntimeJobListIs48WordsFollowedByAnotherGlobal](../behaviors/RuntimeJobListIs48WordsFollowedByAnotherGlobal.md)
- Reads tables: [RuntimeJobList](../tables/RuntimeJobList.md)

## Notes

The job-change list is the other consumer of the same list; it has 19 cells. The list is addressed through three rip-relative `lea` here (0x1403684B8 hands it to JobList_BuildForPartyUnit, 0x1403687A5 reads the entry, 0x14036885A tests the two flags).

## Open questions

None recorded.
