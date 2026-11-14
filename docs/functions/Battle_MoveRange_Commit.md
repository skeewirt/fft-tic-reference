# Battle_MoveRange_Commit

- **Address:** `0x14027B7F0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_MoveRange_Commit(void)`
- **Callers:** Battle_MoveRange_Build, sub_14027E5D4
- **Callees:** sub_1400D9C44

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns the budgets into the lit set: decides for each of the 512 tiles whether the unit can stop there, counts them and writes the result to the tile table (bit 0x20 of tile byte +5) or to the marking table.

## Behavior

- V: first clears flag 0x10 on the tile of every unit with status byte +0x61 bit 0x20 or 0x04 (KO, Jumping): nobody stops there.
- V: for every tile: clears its mark (tile byte +5 bit 0x20 when the battle manager's dword +6536 is 15, else state bit dword +6536 of the manager's marking table through sub_1400D9C44).
- V: the start tile is never lit.
- V: Teleport mode: a tile with flag 0x20 is lit when the unit can ride (scratch byte 0x141882616). Any mode: a tile with mark byte 3 set is lit when the unit can ride.
- V: otherwise all of: slope <= 2 or no flag 0x02; budget byte non-zero; slope <= 3; tile byte +6 bit 7 clear (a sign test); terrain not 28; depth 0, or a deeper tile when scratch byte 0x141882614 is clear and, for depth 3, scratch byte 0x141882612 is clear and, for depth 4 and more, scratch byte 0x141882613 is clear; terrain not 18 unless scratch byte 0x141882625 is set; tile byte +6 bit 0x02 clear; flag 0x10; and when occupied (0x04) flag 0x20 and the unit can ride.
- V: a lit tile increments g_MoveRangeTileCount and gets its mark set the same two ways.
- V: the routine writes no other tile byte: bits 0x40 and 0x80 of byte +5 belong to the target and action code.

## State touched

- Reads: [g_MoveTileFlags](../globals/g_MoveTileFlags.md), [g_BattleRangeMarks](../globals/g_BattleRangeMarks.md), [g_BattleUnitTable](../globals/g_BattleUnitTable.md), [MoveRangeScratch.can_ride](../structs/MoveRangeScratch.md#can_ride)
- Writes: [BattleTileRecord.flags5](../structs/BattleTileRecord.md#flags5), [g_MoveRangeTileCount](../globals/g_MoveRangeTileCount.md)

## Referenced by

- Called by: [Battle_MoveRange_Build](Battle_MoveRange_Build.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Captures: tile byte +5 bit 0x20 of both layers equals this routine's result in all eight; the tiles of KO units are passed but not lit (one capture depends on it).

## Open questions

? Which callers run with the manager dword +6536 other than 15 (then the tile bits keep an older range).
