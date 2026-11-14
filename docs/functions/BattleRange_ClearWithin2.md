# BattleRange_ClearWithin2

- **Address:** `0x14027EB40`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleRange_ClearWithin2(int x, int y)`
- **Callers:** BattleRange_MarkWeaponReach
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears mark byte 0 (both layers) of every tile within Manhattan distance 2 of (x, y): the minimum range of the 'direct' weapons.

## Behavior

- V: for every map tile computes |dx| + |dy| from (x, y); when it is 2 or less, byte 0 of the mark record and of the record 0x500 bytes later (layer 1) become 0.
- I: together with BattleRange_SpreadDiamond this gives guns, crossbows, harps and books a reach of distance 3 up to the weapon range (harps and books, range 3, reach only distance 3); not yet seen live.

## State touched

- Reads: [g_BattleMapSize](../globals/g_BattleMapSize.md)
- Writes: [BattleRangeMarkRecord.reach](../structs/BattleRangeMarkRecord.md#reach)

## Referenced by

- Called by: [BattleRange_MarkWeaponReach](BattleRange_MarkWeaponReach.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Open questions

None recorded.
