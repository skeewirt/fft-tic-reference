# Battle_MoveRange_InitTiles

- **Address:** `0x14027B530`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_MoveRange_InitTiles(int mode)`
- **Callers:** Battle_MoveRange_Build (mode 1), sub_14027C7B4, sub_14027DDB8, sub_14027E5D4
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the range marks, gives every tile its movement flag byte (slope, standable, blocked), stamps the other units onto their tiles and seeds the unit's own tile with Move + 1.

## Behavior

- V: for each of 528 mark records: bytes 1 and 2 = 0; with mode bit 0 also byte 0 = 0, byte 3 = 0, byte 4 = 0xFF. The last 16 records belong to the 16 blocker entries.
- V: tile flag byte for each of the 512 tiles: 2 when (tile byte +4 & 5) is 1 or 4, and 0x42 when the slope (byte +3 low 5 bits) is also 3 or more; otherwise 0x40 when the slope is above the unit's Jump (scratch byte 0x141882604), else 0.
- V: bit 0x10 (standable) is added when tile byte +6 has neither bit 0x01 nor 0x02 and: the depth (byte +3 >> 5) is 0; or the no-water byte (scratch byte 0x141882611) is 0 and the depth is below 4; or the no-water byte is 0 and the no-deep byte (scratch byte 0x141882613) is 0.
- V: tile byte +6 bit 0x01 adds flag 0x80; in movement mode 0 (Fly) a tile with byte +6 bit 0x02 whose terrain is not 63 gets 0x10.
- V: unless mode is 3, each blocker entry stamps its tile (x + width * y + 256 * layer): mark byte 2 = the entry's index, flag 0x04 (occupied). An entry of the other side (id bit 0x40) loses 0x10 and 0x20 and gets 0x08 only in movement mode 0. An entry of the own side loses 0x08, gets 0x08 back from bit 7 of the entry's layer byte (the unit's facing-byte bit 6, copied by Battle_MoveRangeSetup) unless the acting unit has that bit, and gets 0x20 unless its id has bit 0x20 (0x20 on the tile = a mount the acting unit may take).
- V: a blocker whose unit record byte +0 is 73 turns its tile into blocked: bits 0x10 and 0x80 of the old flags are dropped and 0x80 is set (the mask is built in a register).
- V: mode 1: the start tile (x + 256 * layer + width * y of the scratch) gets budget Move + 1, climb byte 0, flag 0x01, and the pending byte = Move + 1; the direction count is 8 and the variant count 4. When the start tile has flag 0x20 the direction count is 36 and the mount's own mark record (512 + its index) is seeded too.
- V: with mode bit 0 the tile count g_MoveRangeTileCount is zeroed.

## State touched

- Reads: [g_BattleTileTable](../globals/g_BattleTileTable.md), [g_MoveBlockers](../globals/g_MoveBlockers.md), [BattleTileRecord.corners](../structs/BattleTileRecord.md#corners), [BattleTileRecord.slope_depth](../structs/BattleTileRecord.md#slope_depth), [BattleTileRecord.flags6](../structs/BattleTileRecord.md#flags6), [MoveRangeScratch.jump](../structs/MoveRangeScratch.md#jump)
- Writes: [g_MoveTileFlags](../globals/g_MoveTileFlags.md), [g_BattleRangeMarks](../globals/g_BattleRangeMarks.md), [g_MoveRangeTileCount](../globals/g_MoveRangeTileCount.md)

## Referenced by

- Called by: [Battle_MoveRange_Build](Battle_MoveRange_Build.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Flag bits of g_MoveTileFlags: 0x01 frontier, 0x02 one-axis slope, 0x04 occupied, 0x08 a unit that can be stepped onto, 0x10 standable, 0x20 mountable ally, 0x40 steep, 0x80 blocked.

## Open questions

? What unit record byte +0 == 73 is. ? What bit 6 of a unit's facing byte means (the 'stepped onto' case); no capture has it.
