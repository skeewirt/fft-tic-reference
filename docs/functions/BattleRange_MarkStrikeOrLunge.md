# BattleRange_MarkStrikeOrLunge

- **Address:** `0x14027F0D0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleRange_MarkStrikeOrLunge(UnitWorkRecord *unit, uint8 weaponFlags)`
- **Callers:** BattleRange_MarkWeaponReach
- **Callees:** Unit_GetReachHeight, BattleRange_MarkTileInBand

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The melee shapes: the four adjacent tiles (flag 0x80), or two tiles in the four straight lines (flag 0x40 alone), each kept only inside a height band around the unit's reach height.

## Behavior

- V: reads x = unit +0x4F, y = unit +0x50 and H = Unit_GetReachHeight(unit) (half-steps, 0..255).
- V: weaponFlags bit 7 set: BattleRange_MarkTileInBand on (x-1, y), (x+1, y), (x, y-1), (x, y+1) with the band [H - 6, H + 5].
- V: bit 7 clear: the same four tiles with [H - 8, H + 7], then (x-2, y), (x+2, y), (x, y-2), (x, y+2) with [H - 6, H + 7].
- V: the weapon's range byte is not read: the strike reach is 1 and the lunge reach 2 for every weapon; the tile between the unit and a distance-2 tile is not tested.
- I: in whole height steps the strike band is 3 down to 2.5 up, matching the live check (Brice on a sword: a tile 3 steps higher not lit).

## State touched

- Calls: [Unit_GetReachHeight](Unit_GetReachHeight.md), [BattleRange_MarkTileInBand](BattleRange_MarkTileInBand.md)
- Reads: [UnitWorkRecord.tile_x](../structs/UnitWorkRecord.md#tile_x), [UnitWorkRecord.tile_y](../structs/UnitWorkRecord.md#tile_y)

## Referenced by

- Called by: [BattleRange_MarkWeaponReach](BattleRange_MarkWeaponReach.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Open questions

None recorded.
