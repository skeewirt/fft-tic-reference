# g_MoveBlockers

- **Kind:** global
- **Address:** `0x141882680`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[112]`
- **Points to / is a:** [MoveBlockerRecord](../structs/MoveBlockerRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Up to 16 entries of 7 bytes, one per other unit on the map (record MoveBlockerRecord); an unused entry has id 0xFF.

## Referenced by

- Described by tables: [MoveBlockers](../tables/MoveBlockers.md)
- Read by: [Battle_MoveRange_CheckMount](../functions/Battle_MoveRange_CheckMount.md), [Battle_MoveRange_CheckSource](../functions/Battle_MoveRange_CheckSource.md), [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md), [Battle_MoveRange_GapBlocked](../functions/Battle_MoveRange_GapBlocked.md), [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md)
- Written by: [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md)

## Open questions

None recorded.
