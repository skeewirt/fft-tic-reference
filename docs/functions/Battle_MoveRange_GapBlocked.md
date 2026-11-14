# Battle_MoveRange_GapBlocked

- **Address:** `0x14027C3DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Battle_MoveRange_GapBlocked(int columnIndex, uint8 shiftA, uint8 shiftB, uint8 height)`
- **Callers:** Battle_MoveRange_ExpandJump, sub_14027D97C
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Whether a column stops a horizontal jump that passes over it at a given height: anything (tile body or enemy) overlapping the band from the height to height + body blocks, and so does a column that is entirely above.

## Behavior

- V: tests four things: the layer-0 tile, the unit on it, the layer-1 tile, the unit on it.
- V: tile: the blocked flag (bit 7, a sign test) blocks only when the tile is also occupied, otherwise it is ignored; else bottom = the lower of its two edge heights along the jump - 2 * thickness, top = the higher edge + 2 * depth.
- V: unit: only an occupied tile without flag 0x08 whose blocker is of the other side counts; it blocks when its base + 3 lies strictly inside the band; else bottom = its base, top = its top.
- V: blocks when bottom or top lies strictly inside (height, height + body), or when the band is inside [bottom, top].
- V: after the four tests, blocks when the lowest bottom seen is above the height.
- I: a gap is a column whose top is at or below the height the unit jumps from; a wall or a higher floor ends the jump line, an enemy standing in the gap too, an ally does not.

## State touched

- Reads: [g_MoveTileFlags](../globals/g_MoveTileFlags.md), [g_MoveBlockers](../globals/g_MoveBlockers.md), [g_BattleTileTable](../globals/g_BattleTileTable.md), [MoveRangeScratch.body](../structs/MoveRangeScratch.md#body)

## Referenced by

- Called by: [Battle_MoveRange_ExpandJump](Battle_MoveRange_ExpandJump.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Captures: without this test three of eight lit sets are wrong.

## Open questions

None recorded.
