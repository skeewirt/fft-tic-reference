# ItemDisplayInShopAndEquipPanels

- **Kind:** observed behaviour
- **Scope:** the shop lists and the equipment detail panel for an item id
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [ShopItemList_FillRow](../functions/ShopItemList_FillRow.md), [ItemCell_BindIconAndName](../functions/ItemCell_BindIconAndName.md), [EquipDetail_SetHelpText](../functions/EquipDetail_SetHelpText.md), [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [ItemIcon_FormatSmallPath](../functions/ItemIcon_FormatSmallPath.md), [ItemIcon_FormatLargePath](../functions/ItemIcon_FormatLargePath.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What a shop row and the detail panel show for an item, all keyed by the item id: name and description from the Item-en row, price from the item record, icon files named by the id.

## Behavior

- V: the name is ItemTable_GetName(id) and the description ItemTable_GetRow(id) +16: nxd Item-en (table 45) by key.
- V: the price is ShopEntry +24, from the exe item record.
- V: the icons are the files ui/ffto/icon/equip_item_s/textureparts/ei_s_<id>_uitx (list, Icon row 13) and ui/ffto/icon/equip_item/textureparts/ei_<id>_uitx (detail panel, Icon row 12); retail ships ids 0..260.
- V (live read): with the contiguous-keys flag kept on a table whose keys have a gap (Item-en keys 0..260 plus 300), the table had first key 0, last key 300 and 262 rows, so key 300 asked row position 300 and found nothing; the text setters then leave their nodes (I: the Rod's texts the owner saw were left from the previous item).
- V: no remap (IdRemap_Lookup) is on these paths; the list holds the id itself.

## Notes

The icon needs the two files named by the id.

## Open questions

None recorded.
