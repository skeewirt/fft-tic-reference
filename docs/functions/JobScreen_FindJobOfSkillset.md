# JobScreen_FindJobOfSkillset

- **Address:** `0x140367888`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int64 JobScreen_FindJobOfSkillset(void *screen, uint16 skillset, int16 *outJob)`
- **Callers:** sub_140335074
- **Callees:** JobScreen_BuildJobTabRows, sub_140367768

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds which job a secondary skillset belongs to for the selected party unit: the first (job, skillset) pair of the unit's secondary list whose skillset matches, else the unit's own job; then hands (job, skillset) on.

## Behavior

- V: fills a 146-entry stack list of 8-byte entries (word 0 = 0, word 1 = 0xFFFF each), then JobScreen_BuildJobTabRows(g_SelectedUnitIndex, the unit's job word +0x24, tab 0, list, mode 1), which is Unit_CollectJobSkillsetPairs.
- V: scans the returned count for word 1 == skillset; the match's word 0 goes to *outJob; with no match (or a match whose job word is 0xFFFF) *outJob is the unit's job word +0x24.
- V: returns sub_140367768(screen, job, skillset) (the job is -1 when nothing matched).

## State touched

- Calls: [JobScreen_BuildJobTabRows](JobScreen_BuildJobTabRows.md)

## Referenced by

- Observed behaviours: [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md)

## Notes

The call of JobScreen_BuildJobTabRows (0x140367906) fills the frame list, which has 146 entries (145 plus the terminator). I: the name, from the lookup it performs; sub_140367768 and the caller were not read.

## Open questions

? what sub_140367768 does with (job, skillset); which screen sub_140335074 serves.
