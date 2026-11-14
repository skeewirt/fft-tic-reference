# Battle_MoveRange_Build

- **Address:** `0x14027B2F0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_MoveRange_Build(int unitSlot)`
- **Callers:** sub_140203B80 (entering Move), sub_1400D94F8 (the per-frame tile-marking reconcile), sub_14031F92C (AI target range)
- **Callees:** Battle_MoveRangeSetup, Battle_MoveRange_InitTiles, Battle_MoveRange_Expand, Battle_MoveRange_ExpandJump, Battle_MoveRange_Commit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the move range of one unit: sets up the scratch block, seeds the unit's tile with its Move budget, spreads the budget tile by tile and jump by jump, then commits the tiles the unit can stop on. Returns their number.

## Behavior

- V: returns -1 when the slot's unit record is empty (byte +1 is 0xFF).
- V: calls Battle_MoveRangeSetup(slot), then Battle_MoveRange_InitTiles(1).
- V: movement mode 1 (Teleport): writes 1 into budget byte 0 of all 512 range-mark records and skips the spread.
- V: otherwise up to Move passes (scratch byte +6); a pass stops the loop when the 'pending' byte (0x1418827FA) is 0, clears it, then scans layer 0 then layer 1, each by rows (y, then x): for every tile whose flag byte has bit 0x01 it clears the bit, points the scratch at the tile and its mark record, and calls Battle_MoveRange_Expand, then Battle_MoveRange_ExpandJump unless the no-jump byte (scratch byte 0x14188261D) is set; after the first processed tile the direction count goes back to 8.
- V: ends with Battle_MoveRange_Commit, copies the slot to dword_140808DF4, sets dword_1437414A4 = 1 and returns the 16-bit count g_MoveRangeTileCount.
- I: a tile reached later in the scan order than the tile that reached it is processed in the same pass, an earlier one in the next pass; the pass limit equals Move, the longest possible path, so it does not cut a range short (the eight captures give the same result with unlimited passes).

## State touched

- Calls: [Battle_MoveRangeSetup](Battle_MoveRangeSetup.md), [Battle_MoveRange_InitTiles](Battle_MoveRange_InitTiles.md), [Battle_MoveRange_Expand](Battle_MoveRange_Expand.md), [Battle_MoveRange_ExpandJump](Battle_MoveRange_ExpandJump.md), [Battle_MoveRange_Commit](Battle_MoveRange_Commit.md)
- Reads: [g_BattleUnitTable](../globals/g_BattleUnitTable.md), [g_MoveTileFlags](../globals/g_MoveTileFlags.md)
- Writes: [g_BattleRangeMarks](../globals/g_BattleRangeMarks.md), [g_MoveTileFlags](../globals/g_MoveTileFlags.md)

## Referenced by

- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

All state is global (the scratch block at 0x141882600, g_MoveTileFlags, g_BattleRangeMarks), so a second build for another unit overwrites it; only the committed tile bits stay.

## Open questions

? Which of the three callers runs when the cursor hovers another unit (the red squares of an enemy's range).
