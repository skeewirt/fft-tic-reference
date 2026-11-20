# AttackWeaponReach

- **Kind:** observed behaviour
- **Scope:** battle: the tiles the Attack command can target, from the equipped weapon or bare hands
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [BattleRange_MarkAttack](../functions/BattleRange_MarkAttack.md), [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md), [BattleRange_MarkStrikeOrLunge](../functions/BattleRange_MarkStrikeOrLunge.md), [BattleRange_MarkArcReach](../functions/BattleRange_MarkArcReach.md), [BattleRange_SpreadDiamond](../functions/BattleRange_SpreadDiamond.md), [BattleRange_ClearWithin2](../functions/BattleRange_ClearWithin2.md), [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md), [BattleRange_FlagTargetTiles](../functions/BattleRange_FlagTargetTiles.md), [ItemWeaponRecord](../structs/ItemWeaponRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which tiles a unit's basic Attack can target: one weapon is chosen, its flag byte picks one of four shapes (strike, lunge, direct, arc), heights are compared in half-steps, the unit's own tile and some flagged tiles are removed.

## Behavior

- V: weapon = the item at unit +0x20; if empty (0xFF) or not below 0x105, the item at +0x24; if that too, item 0 = bare hands (range 1, flags 0x88). Toad (+0x63 bit 0x02) always uses item 0. With two weapons only the +0x20 one decides the reach.
- V: flags bit 0x80 (strike: bare hands, knives, swords, katanas, axes, rods, staves, flails, bags): the four adjacent tiles whose target height is within [H - 6, H + 5] half-steps of the attacker's reach height H.
- V: flags bit 0x40 without 0x80 (lunge: spears, poles, cloths): the four adjacent tiles within [H - 8, H + 7] and the four tiles two away in straight lines within [H - 6, H + 7]; no diagonal, the tile between is not tested.
- V: flags bit 0x20 without 0xC0 (direct: guns 8, crossbows 4, harps 3, books 3): every tile at Manhattan distance 3 up to the range, any height.
- V: none of 0xE0 (arc: bows, flags 0x15, range 5): every tile at distance d >= 3 with d - trunc((H - t) / 4) <= range, t the target's half-step height.
- V: target height t = (b3 & 0x1F) + 2 * (b2 + (b3 >> 5)) of the target tile in its own layer; H = (b3 & 0x1F) + 2 * b2 of the attacker's tile, +2 when mounted, +2 when floating (+0x9E bit 3 or status Float), plus the depth term only for floating or +0x9E bits 7 / 6 (Unit_GetReachHeight).
- V: both layers of a tile are judged separately; the attacker's own tile is removed (BattleRange_MarkAttack); tiles with byte +6 bit 0x02 lose their mark, and tiles with byte +6 bit 0x01 or surface 0x3F are not flagged targetable.
- V: the weapon's range byte is used only by the direct and arc shapes; strike reach is always 1 and lunge reach always 2.
- I: 'H - 6 .. H + 5' in whole steps = a target 3 steps lower up to 2.5 steps higher for a strike; matches the live note that from height 0 a target 3 higher was not yellow.
- I: the shapes do not look at units: a tile is a target whether empty or occupied (live: yellow tiles include empty ones).

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? Not yet seen live: the minimum distance 3 of direct weapons (guns, crossbows, harps, books), the bow height bonus, the lunge bands. ? What decides white versus red-with-slash outside the yellow set (not in these builders).
