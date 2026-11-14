# JobScreen_OpenJobPage

- **Address:** `0x1402B9FB8`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobScreen_OpenJobPage(uint16_t jobId, unsigned arg, bool flag)`
- **Callers:** JobScreen_UpdateState
- **Callees:** sub_14028A6E8, sub_14028A770, sub_140367AA0, sub_14012EF90, sub_14012F000, sub_14028D8F4, sub_1402A286C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds and shows the ability page of a job on the job screen: collects the unit's ability rows for the job and fills the page lists.

## Behavior

- V: reads the current party unit (g_PartyUnits[word_141811428]); when its job (unit+36) equals jobId and it is not dead (+62 <= 0) the unit's job-level word (+94) is used, otherwise -1.
- V: builds the ability list with sub_14028A6E8 (no unit data) or sub_14028A770, up to 146 entries of 8 bytes, mode 7.
- V: for each entry calls sub_140367AA0 and the page-list adders sub_14012EF90 / sub_14012F000 of the list addon.
- V: ends by selecting the first page row (sub_14028D8F4) when `flag` is set and rows exist, or clearing it (sub_1402A286C).
- I: purpose from the call pattern; only caller is JobScreen_UpdateState (0x368D4A, 0x368E85).

## State touched

- Calls: [sub_140367AA0](sub_140367AA0.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [JobScreen_UpdateState](JobScreen_UpdateState.md)

## Open questions

Meaning of `arg` (passed through as the page/tab selector).
