# g_RuntimeJobList

- **Kind:** global
- **Address:** `0x143C51890`
- **Type:** `data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint16[48]: job id (low 13 bits) | 0x2000 locked | 0x4000 released by another member (mode 3) / current (mode 2); 0xFFFF ends it.

## Referenced by

- Described by tables: [RuntimeJobList](../tables/RuntimeJobList.md)
- Observed behaviours: [RuntimeJobListCanLiveInAnyBlockWithinReach](../behaviors/RuntimeJobListCanLiveInAnyBlockWithinReach.md), [RuntimeJobListIs48WordsFollowedByAnotherGlobal](../behaviors/RuntimeJobListIs48WordsFollowedByAnotherGlobal.md)
- Read by: [JobList_IsSelectedEntryUnflagged](../functions/JobList_IsSelectedEntryUnflagged.md), [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [sub_1401321FC](../functions/sub_1401321FC.md)

## Open questions

None recorded.
