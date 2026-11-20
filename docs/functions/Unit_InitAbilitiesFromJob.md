# Unit_InitAbilitiesFromJob

- **Address:** `0x1402771C8`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void Unit_InitAbilitiesFromJob(uint8_t *work, uint8_t *spawn, void *arg3, void *arg4)`
- **Callers:** Unit_BuildFromRecord
- **Callees:** Mem_Free and others in the part not read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a unit work record's skillset and innate ability words from its job row (head read: the skillset choice and the innate copy).

## Behavior

- V: the job is work[3]; job 0xA1 uses row 164 when the low nibble of work+238 is 8 or more. With no spawn record it clears +20 and returns.
- V: the skillset byte at +18 is the spawn record's byte at +29 when that byte is 1 to 254, else the job row's byte 0 (row = JobTable + 49 * job).
- V: the job id is stored in a stack slot (rsp+0x48) and the four innate ability words at +10 are built from row bytes 1..8 of the row of that stored job, after the (not read here) middle part that handles the unit's team bits and the learned-ability bytes at +162..+227.
- V: for a unit built from a spawn record, the OverrideEntryData row (third argument) is read: its array at +0x4C (granted_abilities: offset dword +0x4C, count +0x50, i32 elements, low 16 bits used), its array at +0x54 (withheld_abilities: offset +0x54, count +0x58) and its byte +0x9A (free_abilities). List 1 is the spawn record's reaction / support / movement words (below 0x1FE) plus the granted array, list 2 the withheld array.
- V: both lists and the byte +0x9A are passed to Unit_QueueJobAbilitiesToLearn for each pair of generic jobs (see the behaviour EntryAbilityListsOfPreplacedUnits).
- V (2026-11-10): for a human unit (c + 6 & 0xC0) built from a spawn record, its loop over the level bytes c + 228..237 gives job indices 0..19 their starting JP (Unit_InitJobJp) and queues their abilities (Unit_QueueJobAbilitiesToLearn).
- V: the spawn record's three R / S / M words join the learn queue only below 0x1FE (dx, shared by the three compares at 0x1402772E2, 0x1402772F3, 0x140277307).

## State touched

- Calls: [Mem_Free](Mem_Free.md)

## Referenced by

- Called by: [Unit_BuildFromRecord](Unit_BuildFromRecord.md)
- Observed behaviours: [EntryAbilityListsOfPreplacedUnits](../behaviors/EntryAbilityListsOfPreplacedUnits.md), [NewUnitsGetStartingJpInEveryJob](../behaviors/NewUnitsGetStartingJpInEveryJob.md), [SpawnRecordPassiveWords](../behaviors/SpawnRecordPassiveWords.md)

## Notes

Only the head and the final innate copy were read. At 0x140277234 the job is in rcx on the path that reads the row's skillset, which is also what the stack slot is filled from; the stack slot (rsp+0x48) is read at 0x1402774AE.

## Open questions

The middle part (team bits 0xC0 handling, the learned-ability bytes) was not studied.
