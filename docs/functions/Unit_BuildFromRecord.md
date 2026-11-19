# Unit_BuildFromRecord

- **Address:** `0x140275CA4`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Unit_BuildFromRecord(uint8_t *work, uint8_t *spawn, int arg3, int mode, const uint8_t *overrideRow)`
- **Callers:** Battle_PlaceEntryUnits (battle slot i from entry i), sub_1402841D0 (new-game save records from the entry block, a stack work record), Battle_RebuildUnitInPlace (mode 130, no spawn record)
- **Callees:** Unit_ApplySpawnRecord, UnitWork_InitFromSpawnRecord, Unit_InitAbilitiesFromJob, Unit_ComputeStats, UnitWork_ApplyStartingEquipment, sub_140276DF4, sub_1402757B0, sub_1401EA910, sub_14027788C, sub_1402760E8, sub_14002630C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a unit work record from a spawn record: applies the record, sets up job state, abilities and growth, computes the stats and the starting equipment.

## Behavior

- V: unless mode is 130 it first clears several work fields (+65, +396, +436, +440, +443, +492, +500) and calls Unit_ApplySpawnRecord; a non-zero result returns -1.
- V: then (for mode 130, or by the record's own flags) UnitWork_InitFromSpawnRecord, Unit_InitAbilitiesFromJob and sub_140276DF4 run, five stat pointers (+123, +126, +129, +132, +135) go to sub_1402757B0, and 10 bytes of the job row from row offset 14 (growth pairs) are copied to +138 (job 0xA1 uses row 164 when the low nibble of +238 is 8 or more).
- V: Unit_ComputeStats runs with work+2 temporarily 0xFE (when it was 0xFF); the starting equipment is applied when mode is not 130 and work+2 is above 19.
- V: for a unit of team 0..3 the first save record with that team (byte 0 below 4, byte +1 not 0xFF) supplies bits of the word at work+8 (its +5 and +6 bytes).
- V: the fifth argument (kept in rbp from 0x140275CBF) is passed to UnitWork_InitFromSpawnRecord as its third: the entry's OverrideEntryData row from Battle_PlaceEntryUnits, null from sub_1402841D0 and Battle_RebuildUnitInPlace (2026-11-09).
- V: UnitWork_ApplyStartingEquipment is called with (work, entry) at the end (rcx is set before the leaf sub_14027788C, which does not write it); the gate is mode not 130 and work +2 above 0x13.

## State touched

- Calls: [Unit_ApplySpawnRecord](Unit_ApplySpawnRecord.md), [UnitWork_InitFromSpawnRecord](UnitWork_InitFromSpawnRecord.md), [Unit_InitAbilitiesFromJob](Unit_InitAbilitiesFromJob.md), [Unit_ComputeStats](Unit_ComputeStats.md), [UnitWork_ApplyStartingEquipment](UnitWork_ApplyStartingEquipment.md), [sub_1401EA910](sub_1401EA910.md)

## Referenced by

- Appears in flows: [ScriptedBattleUnitsFromEntries](../flows/ScriptedBattleUnitsFromEntries.md)
- Called by: [Battle_PlaceEntryUnits](Battle_PlaceEntryUnits.md)
- Observed behaviours: [PreplacedUnitsStartWithOneByteItems](../behaviors/PreplacedUnitsStartWithOneByteItems.md)

## Notes

The row offset for the growth copy is computed at 0x140275DDF; r8 holds the offset (before the table base is added) at 0x140275DEA.

## Open questions

What the last block (the save record lookup and the +8 word) is for (? by name only).
