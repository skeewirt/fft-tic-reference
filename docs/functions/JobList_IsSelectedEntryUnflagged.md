# JobList_IsSelectedEntryUnflagged

- **Address:** `0x140367F00`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `uint64_t JobList_IsSelectedEntryUnflagged(void)`
- **Callers:** JobScreen_UpdateState
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether the runtime-list entry under the list cursor lacks the 0x4000 flag (the 'current job' flag), when the list has two or more jobs.

## Behavior

- V: `g_RuntimeJobListLen >= 2 ? (~g_RuntimeJobList[g_JobListSelectedEntry] & 0x4000) >> 14 : 0`.
- V: g_JobListSelectedEntry (word_143C51880, int16) has six references: reads in this function (0x140367F0D, after the early return of a list shorter than 2) and JobScreen_UpdateState (0x140368CF5, 0x140368D2D); writes at 0x140368C45, 0x140368E74 and 0x140368FE4, all in JobScreen_UpdateState.
- V: with a scrolled list the stored value must be the entry (index into g_RuntimeJobList); the stock game stores a cell index, which equals the entry only for lists of 19 or fewer.

## State touched

- Reads: [g_JobListSelectedEntry](../globals/g_JobListSelectedEntry.md), [g_RuntimeJobList](../globals/g_RuntimeJobList.md), [g_RuntimeJobListLen](../globals/g_RuntimeJobListLen.md), [JobListWord.current_job](../structs/JobListWord.md#current_job)

## Referenced by

- Called by: [JobScreen_UpdateState](JobScreen_UpdateState.md)
- Observed behaviours: [RuntimeJobListCanLiveInAnyBlockWithinReach](../behaviors/RuntimeJobListCanLiveInAnyBlockWithinReach.md), [RuntimeJobListIs48WordsFollowedByAnotherGlobal](../behaviors/RuntimeJobListIs48WordsFollowedByAnotherGlobal.md)
- Reads tables: [RuntimeJobList](../tables/RuntimeJobList.md)

## Notes

Global: g_JobListSelectedEntry at 0x143C51880, int16, cursor position the job screen last chose. A leaf function without unwind data; its `lea` of g_RuntimeJobList is at 0x140367F15. The function returns early (ret at 0x140367F0C) for a list shorter than 2; the 0x4000 test and the list read follow that return, so a scan that stops at the first ret does not see them; the other addresses in the second bullet are in JobScreen_UpdateState.

## Open questions

None recorded.
