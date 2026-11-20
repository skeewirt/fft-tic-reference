# Battle_MoveRangeSetup

- **Address:** `0x14027ADB8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_MoveRangeSetup(int unit_slot)`
- **Callers:** Battle_MoveRange_Build, sub_14027C7B4, sub_14027E5D4
- **Callees:** Battle_MoveRange_WeatherCost, Unit_HasStatusGroup

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Prepares the globals the move-range expansion reads: it copies the acting unit move, jump, stance and status data into the range scratch block and fills the sixteen-entry blocker table.

## Behavior

- V: the argument is a battle unit slot; the unit record is the 0x200-byte entry at 0x141853CE0 plus slot times 0x200 (base by lea, stride by shl 9).
- V: it writes the slot to the range scratch byte and stores the constant 0x10100 and a zero byte beside it before reading the unit.
- V: unit bytes +0x4F, +0x50 and +0x51 are copied to the scratch block.
- V: the move and jump values are read from the unit fields at +0x42 and +0x43, per the move-range study.
- V: the blocker table (g_MoveBlockers, 16 entries of 7 bytes, the write pointer starts at 0x141882682) is filled from the unit table: every unit that is present, has none of status byte +0x61 bits 0x64 (Crystal, KO, Jumping) nor +0x62 bit 0x01 (Chest) and is not the acting unit gets an entry (record MoveBlockerRecord): tile, layer, id with the other-side bit 0x40 and the not-a-mount bit 0x20, body height, base and top height.
- V: a job in the 94..96 range decides mounts, not size: the acting unit's scratch byte +0x15 is 1 when its job is 94..96 and Unit_HasStatusGroup(unit, 10) is false; another unit of such a job with no group-10 status and a zero mount byte gets no bit 0x20 in its id (a mount the acting unit may take).
- V: Unit_HasStatusGroup is called only with group 10; Battle_MoveRange_WeatherCost (sub_14027AD6C) returns the cost 1..3 used for the terrain-cost entries that are 0 in the chosen set.
- V: movement mode, body height, the water bytes and the terrain costs are derived from the unit word at +0x9C (its high byte is +0x9D, read as one word), byte +0x9E and status byte +0x63 as listed on the record MoveRangeScratch; Jump is capped at 7 and Move at 124.
- V: a unit whose mount byte (+0x1B4) has bit 7 and names the acting slot is skipped and adds 2 to the acting unit's body height.
- I: this is the setup half of the move-range builder; the expansion itself is Battle_MoveRange_Build.

## State touched

- Calls: [Battle_MoveRange_WeatherCost](Battle_MoveRange_WeatherCost.md), [Unit_HasStatusGroup](Unit_HasStatusGroup.md)
- Reads: [UnitWorkRecord.move](../structs/UnitWorkRecord.md#move), [UnitWorkRecord.jump](../structs/UnitWorkRecord.md#jump), [UnitWorkRecord.move_flags](../structs/UnitWorkRecord.md#move_flags), [UnitWorkRecord.move_flags_d](../structs/UnitWorkRecord.md#move_flags_d), [UnitWorkRecord.move_flags_c](../structs/UnitWorkRecord.md#move_flags_c), [UnitWorkRecord.side](../structs/UnitWorkRecord.md#side), [UnitWorkRecord.mount](../structs/UnitWorkRecord.md#mount), [UnitWorkRecord.status_16_23](../structs/UnitWorkRecord.md#status_16_23), [g_MoveTerrainCostSets](../globals/g_MoveTerrainCostSets.md), [g_BattleMapSize](../globals/g_BattleMapSize.md), [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)
- Writes: [g_MoveRangeScratch](../globals/g_MoveRangeScratch.md), [g_MoveBlockers](../globals/g_MoveBlockers.md), [g_MoveTerrainCost](../globals/g_MoveTerrainCost.md), [MoveRangeScratch.mode](../structs/MoveRangeScratch.md#mode), [MoveBlockerRecord.id](../structs/MoveBlockerRecord.md#id)

## Referenced by

- Called by: [Battle_MoveRange_Build](Battle_MoveRange_Build.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md), [UnitThatBlocksItsAlliesInMoveRanges](../behaviors/UnitThatBlocksItsAlliesInMoveRanges.md)

## Notes

Whole function read (1336 bytes). The range scratch globals and the blocker table are the ones the C5 cursor/range study names. Revised 2026-11-09 with the full read: the earlier lines about a large-monster bit and about sub_14027AD6C clearing state were wrong.

## Open questions

None recorded.
