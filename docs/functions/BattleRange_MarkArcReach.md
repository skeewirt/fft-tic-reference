# BattleRange_MarkArcReach

- **Address:** `0x14027EE40`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleRange_MarkArcReach(UnitWorkRecord *unit, uint8 range)`
- **Callers:** BattleRange_MarkWeaponReach
- **Callees:** Unit_GetReachHeight

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The bow shape: tiles at Manhattan distance 3 or more whose distance, shortened by a quarter of the height the unit stands above them, is within the weapon range.

## Behavior

- V: H = Unit_GetReachHeight(unit); for every map tile at distance d = |dx| + |dy| >= 3 from the unit's tile and for each layer: t = (b3 & 0x1F) + 2 * (b2 + (b3 >> 5)) as an 8-bit value; mark byte 0 = 1 when d - (H - t) / 4 <= range, with signed division truncated toward zero.
- V: tiles nearer than 3 are not marked by it.
- I: in whole steps every 2 steps of height above the target add one tile of reach and every 2 steps below remove one.

## State touched

- Calls: [Unit_GetReachHeight](Unit_GetReachHeight.md)
- Reads: [g_BattleMapSize](../globals/g_BattleMapSize.md), [BattleTileRecord.height](../structs/BattleTileRecord.md#height), [BattleTileRecord.slope_depth](../structs/BattleTileRecord.md#slope_depth)
- Writes: [BattleRangeMarkRecord.reach](../structs/BattleRangeMarkRecord.md#reach)

## Referenced by

- Called by: [BattleRange_MarkWeaponReach](BattleRange_MarkWeaponReach.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Open questions

None recorded.
