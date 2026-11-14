# g_BattleRangeMarks

- **Kind:** global
- **Address:** `0x1418004E0`
- **Type:** `uint8[2560]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Range-mark array: 512 records of 5 bytes, index x + y * width + 256 * layer (layer 1 at +0x500). Byte 0 = in reach (a spread value or 1), byte 1 = spread frontier; written by the BattleRange_* builders, read by BattleRange_FlagTargetTiles.

## Referenced by

- Described by tables: [BattleRangeMarks](../tables/BattleRangeMarks.md)
- Read by: [Battle_MoveRange_Commit](../functions/Battle_MoveRange_Commit.md)
- Written by: [BattleRange_MarkAttack](../functions/BattleRange_MarkAttack.md), [Battle_MoveRange_Build](../functions/Battle_MoveRange_Build.md), [Battle_MoveRange_CheckMount](../functions/Battle_MoveRange_CheckMount.md), [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md), [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md)

## Open questions

None recorded.
