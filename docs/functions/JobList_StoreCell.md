# JobList_StoreCell

- **Address:** `0x14012EC5C`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobList_StoreCell(JobListAddon *addon, JobRecord *rec, int index)`
- **Callers:** JobTree_FillJobRecords
- **Callees:** JobList_ApplyCellRecord, JobList_OnCursorChanged, JobTreePanel_SetJobIcon

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a 148-byte job record into cell `index` of the job-change list (addon+0x2280+148*index); `if (index >= 19) return` (cmp at 0x14012EC81).

## Behavior

- V: 19 UI slots only; any index from 19 up returns without storing.
- V: then applies the cell through JobList_ApplyCellRecord (the cell gadget, or the detail gadget at +16832 in the browsing states), which registers the record's render slot (+0x5C) to the cell's Unit node.
- V: in modes <= 2 a record with showUse (+141) set moves the cursor (+19016) to this cell (to 0 in states 1..3).

## State touched

- Calls: [JobList_ApplyCellRecord](JobList_ApplyCellRecord.md), [JobList_OnCursorChanged](JobList_OnCursorChanged.md), [JobTreePanel_SetJobIcon](JobTreePanel_SetJobIcon.md)
- Reads: [JobRecord.state](../structs/JobRecord.md#state), [JobRecord.showUse](../structs/JobRecord.md#showuse)
- Writes: [JobRecord.jobId](../structs/JobRecord.md#jobid), [JobRecord.state](../structs/JobRecord.md#state), [JobRecord.showUse](../structs/JobRecord.md#showuse)

## Notes

None recorded.

## Open questions

None recorded.
