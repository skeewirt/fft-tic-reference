# Party_CountMasteredJobs

- **Address:** `0x140348828`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int Party_CountMasteredJobs(uint8_t *learnedBits)`
- **Callers:** UnitWork_StoreToSaveSlot
- **Callees:** Skillset_BuildAbilityList, Job_IdToIndex, BitReader_ReadBits

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counts the generic jobs whose every ability is learned and returns half of that count, capped at 7.

## Behavior

- V: walks the job ids 74..93 except 74, 75 and 93; for each, the 24-entry ability list of its JobTable row's skillset (Skillset_BuildAbilityList, mask 15) and the learned bits at learnedBits + 3 x Job_IdToIndex(job).
- V: a job counts when no listed ability has its learned bit clear; the result is count / 2, at most 7.
- V: the JobTable row guard (id >= 0xAE -> no row) never fires: the loop stays below 0x5E.

## State touched

- Calls: [Skillset_BuildAbilityList](Skillset_BuildAbilityList.md), [Job_IdToIndex](Job_IdToIndex.md)

## Referenced by

- Called by: [UnitWork_StoreToSaveSlot](UnitWork_StoreToSaveSlot.md)
- Observed behaviours: [UnlockMaskStreamRunsIntoLearnedBitsPastIndex23](../behaviors/UnlockMaskStreamRunsIntoLearnedBitsPastIndex23.md)

## Notes

The job id bound stays 0xAE, so only the jobs the game ships are counted here.

## Open questions

None recorded.
