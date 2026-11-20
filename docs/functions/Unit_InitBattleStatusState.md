# Unit_InitBattleStatusState

- **Address:** `0x140278E0C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `unsigned int64 Unit_InitBattleStatusState(UnitWorkRecord *unit, int reset)`
- **Callers:** Battle_RebuildUnitTable, Battle_BuildRosterTeam, Battle_AddJoinedUnit, Battle_PlaceEntryUnits
- **Callees:** Unit_ReinitStatusCountdowns

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up the status state of a unit that has just been built into the battle: the applied set, the countdowns and the KO counter.

## Behavior

- V: sets +0x40 to 1 when it is 0; with reset it clears the word +0x194 and the byte +0x196.
- V: derives the applied set from the effective one: +0x1EF = +0x61 & ~+0x57 (five bytes; a loop from the +0x61 base: +398 and -10 from it).
- V: zeroes the 16 countdown bytes +0x66..+0x75 (one 16-byte store at +0x66) and sets the KO counter +0x07 to 0xFF when +5 bit 2 or +6 bits 0x09 are set, else 3; then calls Unit_ReinitStatusCountdowns.

## State touched

- Calls: [Unit_ReinitStatusCountdowns](Unit_ReinitStatusCountdowns.md)
- Reads: [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective), [UnitWorkRecord.innate_status_a](../structs/UnitWorkRecord.md#innate_status_a)
- Writes: [UnitWorkRecord.applied_status](../structs/UnitWorkRecord.md#applied_status), [UnitWorkRecord.status_countdown](../structs/UnitWorkRecord.md#status_countdown), [UnitWorkRecord.ko_counter](../structs/UnitWorkRecord.md#ko_counter)

## Referenced by

- Called by: [Battle_AddJoinedUnit](Battle_AddJoinedUnit.md), [Battle_RebuildUnitTable](Battle_RebuildUnitTable.md)
- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md)

## Notes

Name is ours. Whole function read; a leaf without unwind data. The only place the game derives +0x1EF from +0x61; each caller builds the record (from the save, a spawn record or the roster) right before.

## Open questions

? +0x194 / +0x196.
