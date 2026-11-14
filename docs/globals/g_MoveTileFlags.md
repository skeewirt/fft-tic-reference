# g_MoveTileFlags

- **Kind:** global
- **Address:** `0x141882880`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[512]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per-tile flag byte of the move-range builder: 0x01 frontier, 0x02 one-axis slope, 0x04 occupied, 0x08 unit that can be stepped onto, 0x10 standable, 0x20 mountable ally, 0x40 steep, 0x80 blocked.

## Referenced by

- Described by tables: [MoveTileFlags](../tables/MoveTileFlags.md)
- Read by: [Battle_MoveRange_Build](../functions/Battle_MoveRange_Build.md), [Battle_MoveRange_CheckSource](../functions/Battle_MoveRange_CheckSource.md), [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md), [Battle_MoveRange_Commit](../functions/Battle_MoveRange_Commit.md), [Battle_MoveRange_GapBlocked](../functions/Battle_MoveRange_GapBlocked.md)
- Written by: [Battle_MoveRange_Build](../functions/Battle_MoveRange_Build.md), [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md), [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md)

## Open questions

None recorded.
