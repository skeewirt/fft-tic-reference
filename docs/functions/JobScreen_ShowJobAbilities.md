# JobScreen_ShowJobAbilities

- **Address:** `0x1402BA1FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JobScreen_ShowJobAbilities(int16 job, uint8 flag)`
- **Callers:** JobScreen_UpdateState
- **Callees:** JobRecord_FromJobId, JobScreen_BuildJobTabRows, sub_14028A770, sub_140367AA0, sub_140116140

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the job screen's detail panel for a job: the skillset header row and the four ability tabs of the current party unit.

## Behavior

- V: the unit is g_PartyUnits[word_141811428]; when it is not in a special state (+62 <= 0) and the job is its own, the header shows its secondary skillset (+94), otherwise the job's JobTable row skillset (row guard: job < 0x40 + 0x6E, built in a register).
- V: adds the header record (JobCommand row of the skillset, JobRecord_FromJobId) to the UI list, then for tabs 0..3 the rows of JobScreen_BuildJobTabRows (or sub_14028A770 for the own job) through sub_140367AA0.
- V: called from JobScreen_UpdateState with the job of the selected tree / list entry (or -1).

## State touched

- Calls: [JobRecord_FromJobId](JobRecord_FromJobId.md), [JobScreen_BuildJobTabRows](JobScreen_BuildJobTabRows.md), [sub_140367AA0](sub_140367AA0.md)

## Referenced by

- Reads tables: [JobTable](../tables/JobTable.md)

## Notes

The row bound 0xAE is built in a register as 0x40 + 0x6E by a 3-byte instruction; a job id at or above it gets no header skillset (0), and the tab rows then fault in Job_BuildTabAbilityList.

## Open questions

None recorded.
