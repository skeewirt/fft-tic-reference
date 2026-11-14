# BattleRange_FlagTargetTiles

- **Address:** `0x14027FDD8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleRange_FlagTargetTiles(void)`
- **Callers:** BattleRange_MarkAttack, sub_14027F974
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the range marks into the tile table: sets tile byte +5 bit 0x40 on every marked, targetable tile of both layers and returns how many it set.

## Behavior

- V: for each of the 512 tile records and its mark record: when mark byte 0 is 0, or tile byte +6 has bit 0x01, or (tile byte +0 & 0x3F) == 0x3F, it clears tile byte +5 bit 0x40; otherwise it sets the bit and counts it.
- I: tile byte +0 & 0x3F == 0x3F is a tile with no surface (empty layer-1 records); byte +6 bit 0x01 is a tile that cannot be selected.
- I: tile byte +5 bit 0x40 is the yellow (targetable) mark of the target prompt; the live check of 2026-11-05 read the yellow set from mark byte 0, which this bit follows except on the excluded tiles.

## State touched

- Reads: [BattleRangeMarkRecord.reach](../structs/BattleRangeMarkRecord.md#reach), [BattleTileRecord.surface](../structs/BattleTileRecord.md#surface), [BattleTileRecord.flags6](../structs/BattleTileRecord.md#flags6)
- Writes: [BattleTileRecord.flags5](../structs/BattleTileRecord.md#flags5)

## Referenced by

- Called by: [BattleRange_MarkAttack](BattleRange_MarkAttack.md), [sub_14027F974](sub_14027F974.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Open questions

? Whether the same bit means 'can pass' in Move tile selection (it was seen on allies' tiles there, 2026-11-05).
