# Unit_GetReachHeight

- **Address:** `0x14027EDA4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `uint8 Unit_GetReachHeight(UnitWorkRecord *unit)`
- **Callers:** BattleRange_MarkStrikeOrLunge, BattleRange_MarkArcReach
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The height (in half-steps) the weapon reach rules measure from: the unit's own tile without its water depth, raised when the unit is mounted or floating, with the depth added back for some movement flags.

## Behavior

- V: tile = the record at x + (layer << 8) + width * y (x +0x4F, y +0x50, layer = +0x51 bit 7); h = (b3 & 0x1F) + 2 * b2 (8-bit); depth = 2 * (b3 >> 5).
- V: when unit +0x1B4 has bit 7, h += 2 and the flags below are read from the unit record at slot (+0x1B4 & 0x1F) instead.
- V: when flags byte +0x9E has bit 0x08, or +0x63 has bit 0x40 (status 17, Float), h += 2 and the unit counts as raised.
- V: when depth is not 0: raised or +0x9E bit 7 -> h += depth; else +0x9E bit 6 -> h += depth - 2; else nothing.
- I: +0x1B4 bit 7 = riding (the low bits name the mount) and +0x9E holds movement-ability flags (bit 3 a float-like ability, bits 7 / 6 water movement); the readers here do not name them.

## State touched

- Reads: [g_BattleTileTable](../globals/g_BattleTileTable.md), [BattleTileRecord.height](../structs/BattleTileRecord.md#height), [BattleTileRecord.slope_depth](../structs/BattleTileRecord.md#slope_depth), [UnitWorkRecord.mount](../structs/UnitWorkRecord.md#mount), [UnitWorkRecord.move_flags](../structs/UnitWorkRecord.md#move_flags), [UnitWorkRecord.status_16_23](../structs/UnitWorkRecord.md#status_16_23), [UnitWorkRecord.layer_facing](../structs/UnitWorkRecord.md#layer_facing)

## Referenced by

- Called by: [BattleRange_MarkArcReach](BattleRange_MarkArcReach.md), [BattleRange_MarkStrikeOrLunge](BattleRange_MarkStrikeOrLunge.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Notes

Unlike the target height (BattleRange_MarkTileInBand), the unit's own height leaves the water depth out unless a flag adds it.

## Open questions

? Which movement abilities set +0x9E bits 3, 6 and 7.
