# JobScreen_FillUnitRows

- **Address:** `0x1402B90D4`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobScreen_FillUnitRows(void)`
- **Callers:** sub_1402B9B30, sub_140367644
- **Callees:** JobList_BuildForPartyUnit, sub_1402C0554, sub_140327854, Input_TestAction, sub_1402B9090, JobScreen_ShowPopup, Job_IdToIndex, sub_1402B8FE4, sub_1402B9044, sub_1403278EC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the job menu rows for the selected party unit: the static job record, the level and JP readers and the availability flags.

## Behavior

- V: it initialises the job screen state once, guarded by the flag at 0x140D407CA, and builds the list callbacks.
- V: the selected party slot is the signed word at 0x141811428; the unit pointer is g_PartyUnits[slot].
- V: it reads the job id from the unit and converts it with Job_IdToIndex, then fills the static job record.
- V: the four job menu readers supply the level, current JP, total JP and next-level JP.
- V: JobList_BuildForPartyUnit builds the job rows, and JobScreen_ShowPopup handles the popup state.
- V: Input_TestAction is polled for the menu buttons, and sub_1403278EC draws the resulting rows.
- V: the routine writes the screen state words at 0x141876B00 and the static record, so a second call refreshes rather than rebuilds.
- I: the once-only guard is the same pattern the job screen uses on its other pages; the flag byte is the page-initialised marker.
- ?: which of the four read values maps to which menu column; the column order was not read.

## State touched

- Calls: [JobList_BuildForPartyUnit](JobList_BuildForPartyUnit.md), [sub_1402C0554](sub_1402C0554.md), [Input_TestAction](Input_TestAction.md), [JobScreen_ShowPopup](JobScreen_ShowPopup.md), [Job_IdToIndex](Job_IdToIndex.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_SelectedUnitIndex](../globals/g_SelectedUnitIndex.md), [g_JobTable](../globals/g_JobTable.md)

## Referenced by

- Observed behaviours: [JobListBuilderCallersHold24Words](../behaviors/JobListBuilderCallersHold24Words.md)

## Notes

Whole function read (652 bytes).

## Open questions

None recorded.
