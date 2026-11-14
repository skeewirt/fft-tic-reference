# JobLearnList_ReadSelectedJp

- **Address:** `0x1402B9384`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `uint16_t JobLearnList_ReadSelectedJp(void)`
- **Callers:** JobScreen_BuildLearnList, JobScreen_RefreshLearnList (as a callback)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The JP the Learn Abilities list shows: the selected party unit's JP in the job the Jobs screen has selected.

## Behavior

- V: returns the u16 at g_PartyUnits[g_SelectedUnitIndex] + 202 + 2 * word_14375F088 (the party record's JP words).
- V: word_14375F088 is written only by JobScreen_FillUnitRows: Job_IdToIndex of the selected row's job id (word_14375EFF8).
- V: no code calls it; JobScreen_BuildLearnList (0x1402B9602) and JobScreen_RefreshLearnList (0x1402B9C99) take its address (lea), as the list's JP callback.
- V: a leaf function (no unwind entry).
- V (2026-11-10): its index comes from a global, not from a Job_IdToIndex call of its own.

## Notes

The name is ours (IDB: sub_1402B9384).

## Open questions

None recorded.
