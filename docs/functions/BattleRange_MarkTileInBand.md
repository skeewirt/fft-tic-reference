# BattleRange_MarkTileInBand

- **Address:** `0x14027F1D4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleRange_MarkTileInBand(int x, int y, int lo, int hi)`
- **Callers:** BattleRange_MarkStrikeOrLunge
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets mark byte 0 = 1 for a map tile, separately in each layer, when that layer's target height is inside [max(lo, 0), hi].

## Behavior

- V: does nothing when x or y is outside the map (0 <= x < width, 0 <= y < height, g_BattleMapSize bytes 0 and 1).
- V: lo below 0 is taken as 0.
- V: for layer 0 and layer 1 (tile record + 0x800 * layer, mark record + 0x500 * layer): target height = (b3 & 0x1F) + 2 * (b2 + (b3 >> 5)) with b2, b3 = tile record bytes +2, +3; mark byte 0 = 1 when lo <= height <= hi.
- I: b2 is the tile height in whole steps, b3 bits 0..4 a slope / half step in half-steps and bits 5..7 the water depth (the debugger's HUD height read agrees: 'Height' = b2 + half step + depth), so the target height counts half-steps up to the water surface.

## State touched

- Reads: [g_BattleMapSize](../globals/g_BattleMapSize.md), [BattleTileRecord.height](../structs/BattleTileRecord.md#height), [BattleTileRecord.slope_depth](../structs/BattleTileRecord.md#slope_depth)
- Writes: [BattleRangeMarkRecord.reach](../structs/BattleRangeMarkRecord.md#reach)

## Referenced by

- Called by: [BattleRange_MarkStrikeOrLunge](BattleRange_MarkStrikeOrLunge.md)

## Open questions

None recorded.
