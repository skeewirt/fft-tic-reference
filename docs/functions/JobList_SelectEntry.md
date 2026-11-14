# JobList_SelectEntry

- **Address:** `0x14012F7F4`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobList_SelectEntry(JobListAddon *addon, unsigned idx)`
- **Callers:** sub_140113F40
- **Callees:** UIPosFollow_SetTarget, UIPosFollow_Snap, JobChangeAddon_SetState, sub_140132D48, sub_140132D6C, sub_140132ED4, sub_1400F4BCC (sound)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Handler for screen message 128 (a tree panel was clicked): puts the job-change list cursor on cell `idx`, moves the highlight there and switches the list mode.

## Behavior

- V: does nothing unless `idx <= 0x12` (19 cells); this guard is why a list longer than 19 needs the scroll window before the call.
- V: stores `idx` at addon+19016 (cursor cell), re-targets the two position followers (UIPosFollow_SetTarget + UIPosFollow_Snap) at the selected cell's node, then runs two cell-refresh helpers (sub_140132ED4, sub_140132D6C).
- V: if the mode byte at addon+19012 is 4 the state change goes to mode 2; otherwise the cell's record is read (148-byte records at addon+8904, dword at +60): non-zero -> JobChangeAddon_SetState(addon, 6, 0) and sound 25, zero -> JobChangeAddon_SetState(addon, 3, 0) and sound 14.
- V: only caller is the screen message switch sub_140113F40, case 128, call site 0x14011468D.

## State touched

- Calls: [UIPosFollow_SetTarget](UIPosFollow_SetTarget.md), [UIPosFollow_Snap](UIPosFollow_Snap.md), [JobChangeAddon_SetState](JobChangeAddon_SetState.md), [sub_140132D6C](sub_140132D6C.md), [sub_1400F4BCC](sub_1400F4BCC.md)
- Reads: [JobRecord.state](../structs/JobRecord.md#state)

## Referenced by

- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

Prototype read from the decompile; the argument is a cell index, not a job id and not a runtime-list entry.

## Open questions

What sub_140132ED4 / sub_140132D6C refresh (head only read).
