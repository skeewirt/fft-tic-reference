# UnitWork_InitFromSpawnRecord

- **Address:** `0x14027699C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void UnitWork_InitFromSpawnRecord(UnitWork *c, uint8_t *spawn, const uint8_t *overrideRow)`
- **Callers:** Unit_BuildFromRecord
- **Callees:** Unit_BuildJobUnlockMask, UnitWork_ApplyJobRow, Unit_PickUnlockedJobAtRandom

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a new unit's job state in its work record from a spawn record: job levels, unlock mask, job row and secondary skillset. It holds the stock rule that gives every generic job level 1 to a new unit.

## Behavior

- V: clears the 12 level bytes (C +228..239).
- V: when the spawn record is present, not flagged 0x20 at +1 and its job index (+8) is below 20: the job's level nibble becomes spawn +9 & 0xF; then for the 10 level bytes (indices 0..19) each byte is OR-ed with the JobNeedLevel row of the spawn job (virtual base 0x14067F384 + 12 x index; index 0 uses 0x11 / 0x01, built in a register by a select, not an immediate operand), and every nibble still 0 becomes 1. So every generic job (0..19) starts at level >= 1; indices 20..23 stay 0.
- V: spawn +1 bit 6 clears the low nibble of byte 8 (index 17), bit 7 the high nibble of byte 9 (index 18).
- V: then Unit_BuildJobUnlockMask(levels, flags, C +162, C +500) -> C +159..161 (big-endian), job = spawn +10, UnitWork_ApplyJobRow.
- V: spawn +29 (1..254) sets the skillset byte C +18; spawn +11 is the secondary skillset, 0xFE = the skillset of a random unlocked job (Unit_PickUnlockedJobAtRandom).
- V: with no spawn record: job row 0, C +6 = 0x20, empty unlock mask.
- V: the third argument is the OverrideEntryData row of the entry (Unit_BuildFromRecord's fifth argument, from Battle_PlaceEntryUnits; null from the other callers); it is only passed on to UnitWork_ApplyJobRow, whose UnitWork_AddEntryGrowthBonus reads the row's four bonus arrays.

## State touched

- Calls: [Unit_BuildJobUnlockMask](Unit_BuildJobUnlockMask.md), [UnitWork_ApplyJobRow](UnitWork_ApplyJobRow.md)

## Referenced by

- Appears in flows: [ScriptedBattleUnitsFromEntries](../flows/ScriptedBattleUnitsFromEntries.md)
- Called by: [Unit_BuildFromRecord](Unit_BuildFromRecord.md)
- Observed behaviours: [EntryAbilityListsOfPreplacedUnits](../behaviors/EntryAbilityListsOfPreplacedUnits.md), [EntryGrowthBonusesByPlayMode](../behaviors/EntryGrowthBonusesByPlayMode.md), [NewUnitsGetStartingJpInEveryJob](../behaviors/NewUnitsGetStartingJpInEveryJob.md), [SpawnedUnitsCarryAOneByteJob](../behaviors/SpawnedUnitsCarryAOneByteJob.md)
- Reads tables: [SkillsetTableSpecial](../tables/SkillsetTableSpecial.md)

## Notes

The job comes from one byte, spawn +10 (0x140276B04, stored into C +3 at 0x140276B07), so a spawn names a job id of one byte only (behaviour SpawnedUnitsCarryAOneByteJob).

## Open questions

None recorded.
