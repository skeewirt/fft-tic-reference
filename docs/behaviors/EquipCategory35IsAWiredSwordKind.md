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
- V (seen live 2026-11-23): an item of category 35 in a shop lists under Weapons with its category's name row (nxd UIItemCategory row 35, added) and the category symbol of picture 36 (a pouch); a Squire whose mask has bit 35 lists it among Equippable Weapons, the detail page 3 lights the jobs whose mask has the bit (EquipDetail_Refresh tests bit category of each job row at 0x140786C5A + 9), and in battle the holder's scene object took attack motion type 3 (+338).
- V (code, seen live 2026-11-23): the Enhanced menus draw an item's category symbol as picture (ui category + 1) of the symbol sheet, the ui category being the item's text row +0x24 (nxd Item ui_item_category): it is loaded, 1 is added and the result is stored in the node's +0xF8, in ShopItemList_FillRow (0x1402A3A86; the item row cell of the shop, Inventory and equipment lists) and EquipDetail_Refresh (0x14029FA53; the detail header, whose name comes from UIItemCategory row ui category, read earlier). These are the only two such loads in the code. Changing that value to 3 at both loads drew the Sword's symbol on an item of ui category 35 in the Inventory and the equipment list, with the name still that of row 35.
- V (seen live 2026-11-23): exe.shop.item_category_icon_cells (0x1407155B0) is not read by these menus: its row 35 set to the Sword's cell (104, 128) changed nothing in the Inventory list or detail header.
- V (data): the symbol sheet is ui/ffto/unit/texture/ui_icon_equip_category_uitx.tex (240 x 280, BC7) with the parts file ui/ffto/unit/textureparts/ui_icon_equip_category_uitx.utexpt: part 0 the whole sheet, part k + 1 the 40 x 40 cell k, six to a row (38 parts: cells 0..36; cell 0 is empty, cells 35 and 36 hold two pouch symbols); cells 37..41 of the sheet are empty and have no part. A .utexpt is: +0 the texture path's offset, +4 the part table's offset (12), +8 the part count; 20 bytes per part: the name's offset (from the part), x0, y0, x1, y1; the path and the names follow the table.
- V (seen live 2026-11-23): a parts file with five more parts (cells 37..41) and a sheet with pictures in those cells drew part 38 for an item whose symbol value was 37 in the Inventory row, the equipment list row and both detail headers.
- V (data): the world map location panel (ui/ffto/worldmap/worldmap_base_info.uib, component TownInfo) has 31 nodes IconEquipCategoryNN (70 x 70, 70 apart, References to the component IconEquipCategory with states On and Off) in four layers: LayerWepon (17 in a 6-column grid of 3 rows, the last cell of row 3 at (354, 188) empty), LayerArmor (6), LayerAccessory (5 in a row, (354, 48) empty) and LayerOther (3, (214..354, 48) empty); each node's picture is Icon row 14 (equip_cat/textureparts/ec_%03d_uitx, 64 x 64; the game ships ec_001..ec_034).
- V (seen live 2026-11-23): a node IconEquipCategory35 added to LayerWepon at (354, 188) and UIItemCategory row 35 with +20 = 35, with WorldMapLocationPanel_Init's loop and WorldMapLocationPanel_Fill's count run to 40 and their arrays for 35..39 kept elsewhere, showed picture ec_035 in that cell, On or Off by the towns' shops.
- V: UIItemCategory column +20 (unknown14) is the number NN of the node IconEquipCategoryNN that sub_14015F730 (the world map's town information: the categories a town's shop sells) shows for the row; -1 on four stock rows.

## Notes

Seen with a Broadsword copy (power 9) in category 35 held by a Squire of physical attack 3, Faith 56: the hit dealt 3.

## Open questions

? what uses the two stock pouch symbols of cells 35 and 36.
