# g_BattleTileTable

- **Kind:** global
- **Address:** `0x140D8DCB0`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[4096]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle map tile table: 512 records of 8 bytes (flags and movement cost), filled by the map setup from the packed level record and read by the map code.

## Behavior

- V: the map loader writes width/height at 0x140C6AD6A/6B and the readers bound by them.

## Referenced by

- Described by tables: [BattleTiles](../tables/BattleTiles.md)
- Read by: [Battle_MoveRange_CeilingAbove](../functions/Battle_MoveRange_CeilingAbove.md), [Battle_MoveRange_GapBlocked](../functions/Battle_MoveRange_GapBlocked.md), [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md), [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md)
- Written by: [MapBlock_RunCommand](../functions/MapBlock_RunCommand.md), [sub_140248E08](../functions/sub_140248E08.md)

## Open questions

None recorded.
