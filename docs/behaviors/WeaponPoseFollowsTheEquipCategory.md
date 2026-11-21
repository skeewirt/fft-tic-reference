# WeaponPoseFollowsTheEquipCategory

- **Kind:** observed behaviour
- **Scope:** engine (battle sprites, weapon attack motion)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ItemSprite_LoadPalettes](../functions/ItemSprite_LoadPalettes.md), [BattleAnim_SelectWeaponMotion](../functions/BattleAnim_SelectWeaponMotion.md), [EquipSprite_BuildPieces](../functions/EquipSprite_BuildPieces.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

ItemSprite_LoadPalettes stores a weapon's animation type at object +338 from its equipment category (item record byte +5): category 35 becomes 3, any other category of 32 or more becomes 21, and a category below 32 is its own type; BattleAnim_SelectWeaponMotion picks the attack motion from that type, and types 19..23 have no motion.

## Behavior

- V: ItemSprite_LoadPalettes loads the two palettes the item picks (its palette row byte 0, a nibble each) into rows 5 and 6 of the object's palette bank (object +8) with sub_1402F7594(palette, row, bank, 0), which copies the 16 colours at once (sub_1402F74D8), and stores the item id at object +336.
- V: the same function writes the type to object +338; EquipSprite_BuildPieces adds a per-type offset (state +32 table indexed by +338) to the frame it draws.
- V (table): exe.battle.weapon_hit_sound_cues holds 3 rows of 32 entries.
- V (data): the job rows' equipment mask (exe.job.equip_flags, 5 bytes) has 40 category bits; the stock jobs set bits 0..31, 35 and 36, and bits 32, 33, 34, 37, 38 and 39 are set by no stock job; the items that have a palette row use categories 0..19, 32 and 33.

## Notes

A new category of 32 or more therefore draws with type 21 (no attack motion) unless its type is set another way.

## Open questions

? how exe.battle.weapon_hit_sound_cues is indexed (by animation type, likely, from its 32 entries); ? which menus read the category (the equipment screen's category icons IconEquipCategory%02d).
