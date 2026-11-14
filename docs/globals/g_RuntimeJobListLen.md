# g_RuntimeJobListLen

- **Kind:** global
- **Address:** `0x143C510D8`
- **Type:** `data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

int16 length of g_RuntimeJobList (signed compares in the fill loop)

## Referenced by

- Observed behaviours: [RuntimeJobListCanLiveInAnyBlockWithinReach](../behaviors/RuntimeJobListCanLiveInAnyBlockWithinReach.md), [RuntimeJobListIs48WordsFollowedByAnotherGlobal](../behaviors/RuntimeJobListIs48WordsFollowedByAnotherGlobal.md)
- Read by: [JobList_IsSelectedEntryUnflagged](../functions/JobList_IsSelectedEntryUnflagged.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md)
- Written by: [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md)

## Open questions

None recorded.
