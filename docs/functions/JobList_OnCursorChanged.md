# JobList_OnCursorChanged

- **Address:** `0x140131BF8`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobList_OnCursorChanged(JobListAddon *addon, int64_t index, int64_t flag)`
- **Callers:** job list input
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Cursor-change handler of the job-change list (UIAddonFFTOUnitJobChange2).

## Behavior

- V: cursor index at addon+19016, mode at +19008; layout root node at *(addon+88). Called from 0x130FD1 and 0x1303A7.
- V: the grid has 19 cells in rows of 6/7/6; cell gadgets are 256 bytes each at addon+11712 with the cell root node in slot 3 (+24). Records are stored by JobList_StoreCell at addon+0x2280+148*i.

## Referenced by

- Called by: [JobChangeAddon_SetState](JobChangeAddon_SetState.md), [JobList_StoreCell](JobList_StoreCell.md), [sub_140130DF0](sub_140130DF0.md)

## Open questions

None recorded.
