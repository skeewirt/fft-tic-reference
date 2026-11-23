# EquipCategory35IsAWiredSwordKind

- **Kind:** observed behaviour
- **Scope:** engine (items, battle formulas, menus)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_140305A48](../functions/sub_140305A48.md), [ItemSprite_LoadPalettes](../functions/ItemSprite_LoadPalettes.md), [sub_140269554](../functions/sub_140269554.md), [Unit_ApplyEquipment](../functions/Unit_ApplyEquipment.md), [Item_CanUnitEquip](../functions/Item_CanUnitEquip.md), [EquipDetail_Refresh](../functions/EquipDetail_Refresh.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Equipment category 35 has no stock item, but the code treats it as a kind of sword: it draws and sounds as a sword, counts as a sword for the sword flag, and the weapon formula gives it its own attack value, physical attack x (100 - Faith) / 100. Categories 36..39 have none of this.

## Behavior

- V: sub_140305A48 (the weapon attack value of formulas 1 and 2) has a case for category 35: (physical attack x (100 - the unit's byte +45, Faith)) / 100, at least 1; categories 36..39 match no case and leave the value as it was.
- V: ItemSprite_LoadPalettes and sub_140269554 map category 35 to 3 (sword) for the attack motion and the hit sound, any other category of 32 or more to 21 (motion) or 1 (sound).
- V: Unit_ApplyEquipment sets the unit's flag +438 bit 8 for categories 3, 4 and 35.
- V (seen live 2026-11-23): an item of category 35 in a shop lists under Weapons with its category's name row (nxd UIItemCategory row 35, added) and the category icon cell 35 (a pouch); a Squire whose mask has bit 35 lists it among Equippable Weapons, the detail page 3 lights the jobs whose mask has the bit (EquipDetail_Refresh tests bit category of each job row at 0x140786C5A + 9), and in battle the holder's scene object took attack motion type 3 (+338).
- V: UIItemCategory column +20 (unknown14) is the number NN of the node IconEquipCategoryNN that sub_14015F730 (the world map's town information: the categories a town's shop sells) shows for the row; -1 on four stock rows.

## Notes

Seen with a Broadsword copy (power 9) in category 35 held by a Squire of physical attack 3, Faith 56: the hit dealt 3.

## Open questions

? the icon cell the HD equipment lists draw for a category (exe.shop.item_category_icon_cells rows 35 / 36 hold (156, 204) / (168, 204), 37..39 (0, 0)).
