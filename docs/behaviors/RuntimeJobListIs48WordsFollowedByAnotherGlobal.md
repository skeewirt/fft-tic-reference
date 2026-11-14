# RuntimeJobListIs48WordsFollowedByAnotherGlobal

- **Kind:** observed behaviour
- **Scope:** engine (runtime job list)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobList_Build](../functions/JobList_Build.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md), [JobList_IsSelectedEntryUnflagged](../functions/JobList_IsSelectedEntryUnflagged.md), [g_RuntimeJobList](../globals/g_RuntimeJobList.md), [g_RuntimeJobListLen](../globals/g_RuntimeJobListLen.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

g_RuntimeJobList is 96 bytes (48 words) and the next object in memory is g_UIChosenItemId, so the list cannot grow in place; the length is a signed 16-bit word kept at another address.

## Behavior

- V (IDA): g_RuntimeJobList is at 0x143C51890; g_UIChosenItemId is at 0x143C518F0 (list + 0x60) and is read by sub_14036AC38 and written by sub_14036AC74; g_JobListSelectedEntry (int16) is at 0x143C51880, 16 bytes before the list.
- V: the length g_RuntimeJobListLen is a separate int16 at 0x143C510D8; it is written by JobTree_FillJobRecords (two stores, the second sets 1 for a unit hidden from the tree), read by JobList_IsSelectedEntryUnflagged (compare with 2) and by the fill loop (signed 16-bit compare and conditional move).
- V: the list has 10 code references, none outside three functions: JobList_IsSelectedEntryUnflagged (1 lea), JobTree_FillJobRecords (3 lea: 0x1403684B8 passes it to the builder, 0x1403687A5 reads an entry, 0x14036885A tests flags), JobScreen_UpdateState (6 reads through image base + rva + index*2, at 0x140368D06, 0x140368D42, 0x140368DB9, 0x140368E7D, 0x140368EC5, 0x140368F9A).
- V: the stock builder writes at most 22 entries and the 0xFFFF terminator (23 words).

## Open questions

None recorded.
