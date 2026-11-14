# BattleRange_SpreadDiamond

- **Address:** `0x14027EBF8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleRange_SpreadDiamond(uint8 range)`
- **Callers:** BattleRange_MarkWeaponReach, BattleRange_MarkArea, sub_14027F270, sub_14027F5B4, sub_14027F974
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Spreads the seeded marks outward one tile per pass for range passes, so every tile within Manhattan distance range of a seed gets a non-zero mark byte 0; heights are not looked at.

## Behavior

- V: range 0: clears mark byte 1 of every record and returns.
- V: otherwise up to range passes over the layer-0 records (width x height, g_BattleMapSize): each record with byte 1 set clears it and, for its four in-map neighbours whose byte 0 is below its own value v, writes v - 1 into byte 0 of both layers; when v is above 2 it also sets the neighbour's byte 1 so the next pass continues from it.
- V: stops early when a pass sets no byte 1.
- I: with the seed at range + 1 the result is byte 0 = range + 1 - distance for every tile up to distance range: a diamond over the whole map, both layers alike.

## State touched

- Reads: [g_BattleMapSize](../globals/g_BattleMapSize.md)
- Writes: [BattleRangeMarkRecord.reach](../structs/BattleRangeMarkRecord.md#reach), [BattleRangeMarkRecord.frontier](../structs/BattleRangeMarkRecord.md#frontier)

## Referenced by

- Called by: [BattleRange_MarkWeaponReach](BattleRange_MarkWeaponReach.md), [sub_14027F974](sub_14027F974.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Notes

Shared with the ability range builders.

## Open questions

None recorded.
