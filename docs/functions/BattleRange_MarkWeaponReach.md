# BattleRange_MarkWeaponReach

- **Address:** `0x14027EFC0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleRange_MarkWeaponReach(UnitWorkRecord *unit)`
- **Callers:** BattleRange_MarkAttack, sub_14027F974 (abilities whose record byte +3 has bit 0x20)
- **Callees:** Item_GetWeaponRecord, BattleRange_MarkStrikeOrLunge, BattleRange_SpreadDiamond, BattleRange_ClearWithin2, BattleRange_MarkArcReach

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks in the range-mark array the tiles one unit's weapon reaches from its tile: picks the weapon, seeds the unit's tile and runs one of three shape routines chosen by the weapon's flag byte.

## Behavior

- V: weapon: the word at unit +0x20 unless unit +0x63 bit 0x02 (Toad) is set, in which case 0; when that word is 0xFF or not below 0x105 (built as 0xFF + 6 in a register at 0x14027F000, so no 0x105 constant appears) it takes the word at unit +0x24 under the same test; when that fails too, item 0. Only this one item sets the shape (a second weapon is ignored).
- V: Item_GetWeaponRecord of the item; when it returns null (not a weapon) Item_GetWeaponRecord(0) (the bare-hands row: range 1, flags 0x88 in the weapon table data, not in this body).
- V: seeds the unit's tile (index x + y * width, x = unit +0x4F, y = unit +0x50, width = byte 0 of g_BattleMapSize): mark byte 0 = range + 1 in layer 0 and layer 1, mark byte 1 = 1 in layer 0.
- V: flags & 0xC0: BattleRange_MarkStrikeOrLunge(unit, flags); else flags & 0x20: BattleRange_SpreadDiamond(range) then BattleRange_ClearWithin2(x, y); else BattleRange_MarkArcReach(unit, range).
- V: last, clears mark byte 0 of every record (both layers) whose tile record byte +6 has bit 0x02.
- V (data, the weapon table of the pristine executable): flags 0x80 is set on bare hands, knives, ninja blades, swords, knight swords, katanas, axes, rods, staves, flails and bags; 0x40 on spears, poles and cloths; 0x20 on guns, crossbows, harps and books; bows have 0x15 and so take the last branch (0x80 here = bit 7 of the flag byte; the values are table data).

## State touched

- Calls: [BattleRange_MarkStrikeOrLunge](BattleRange_MarkStrikeOrLunge.md), [BattleRange_SpreadDiamond](BattleRange_SpreadDiamond.md), [BattleRange_ClearWithin2](BattleRange_ClearWithin2.md), [BattleRange_MarkArcReach](BattleRange_MarkArcReach.md), [sub_1402B8C74](sub_1402B8C74.md)
- Reads: [UnitWorkRecord.right_weapon](../structs/UnitWorkRecord.md#right_weapon), [UnitWorkRecord.left_weapon](../structs/UnitWorkRecord.md#left_weapon), [UnitWorkRecord.status_16_23](../structs/UnitWorkRecord.md#status_16_23), [UnitWorkRecord.tile_x](../structs/UnitWorkRecord.md#tile_x), [UnitWorkRecord.tile_y](../structs/UnitWorkRecord.md#tile_y), [ItemWeaponRecord.range](../structs/ItemWeaponRecord.md#range), [ItemWeaponRecord.flags](../structs/ItemWeaponRecord.md#flags), [BattleTileRecord.flags6](../structs/BattleTileRecord.md#flags6), [g_BattleMapSize](../globals/g_BattleMapSize.md)
- Writes: [BattleRangeMarkRecord.reach](../structs/BattleRangeMarkRecord.md#reach), [BattleRangeMarkRecord.frontier](../structs/BattleRangeMarkRecord.md#frontier)

## Referenced by

- Called by: [BattleRange_MarkAttack](BattleRange_MarkAttack.md), [sub_14027F974](sub_14027F974.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Notes

The second argument its callers pass is not read. The unit's layer bit (+0x51 bit 7) is not used here: the seed and the shapes mark both layers.

## Open questions

? What tile byte +6 bit 0x02 stands for (a tile no attack may target).
