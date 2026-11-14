# Battle_MoveRange_CheckSource

- **Address:** `0x14027BAC4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_MoveRange_CheckSource(int dirIndex)`
- **Callers:** Battle_MoveRange_Expand, Battle_MoveRange_ExpandJump
- **Callees:** Battle_MoveRange_CeilingAbove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Prepares leaving the current tile in one direction: the height of the edge being left, the headroom above it and the budget record to spend from; returns non-zero when the tile cannot be left that way.

## Behavior

- V: ground case (direction index below 4): exit height = height * 2 + slope * ((corner byte >> shift of the edge left) & 3); the same with the opposite edge's shift gives the back height; their difference is stored as the slope along the step.
- V: headroom = Battle_MoveRange_CeilingAbove(x, y, edge shift, exit height).
- V: returns 3 when the difference is 0 or more and the tile's flag has 0x40 (a steep tile can only be left downhill).
- V: when the tile has water (byte +3 >= 0x20) and the stored movement flags (scratch byte 0x14188261C) have bit 7 or bit 6 (one test of both, mask 0xC0), the exit height rises by 2 * depth, minus 2 when bit 6 (0x40) is set.
- V: the budget record is the tile's own mark record; returns 4 when its budget is below 2, else 0.
- V: unit case (index 4 and above): the blocker entry is the tile's mark byte 2. Index below 8: returns 2 unless the tile flag has 0x08, exit height = the entry's top. Index 8 and above: exit height = the entry's base + (index >> 2) - 2, returns 1 when that is below the tile's edge height. Headroom is taken above exit height - 1 and the budget record is mark record 512 + the entry's index.

## State touched

- Calls: [Battle_MoveRange_CeilingAbove](Battle_MoveRange_CeilingAbove.md)
- Reads: [g_MoveTileFlags](../globals/g_MoveTileFlags.md), [g_MoveBlockers](../globals/g_MoveBlockers.md), [MoveRangeScratch.stored_flags](../structs/MoveRangeScratch.md#stored_flags), [BattleTileRecord.height](../structs/BattleTileRecord.md#height), [BattleTileRecord.corners](../structs/BattleTileRecord.md#corners)

## Referenced by

- Called by: [Battle_MoveRange_Expand](Battle_MoveRange_Expand.md), [Battle_MoveRange_ExpandJump](Battle_MoveRange_ExpandJump.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Heights are in half-steps: a height step is 2, a slope unit is 1 per corner value.

## Open questions

? The unit case is not covered by any capture (it needs a unit with flag 0x08 on its tile, or a mounted start).
