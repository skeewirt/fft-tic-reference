# ShopItemList_FillRow

- **Address:** `0x1402A3578`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ShopItemList_FillRow(ShopItemList *list, GUINode *row, ShopEntry *entry, char gray, char flag, int nameTextId)`
- **Callers:** ShopItemList_DrawRow (sub_1402A57AC), sub_140129D30, sub_1401AB768, sub_1402A6710
- **Callees:** ItemCell_SetItem, UITable_GetRowByKey, GUINode_FindPartByName, UIName_Key, sub_1402A45DC, sub_1402A474C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one row of an item list (the shop's buy and sell lists and three other lists): icon and name, the equipped and owned counts and the category image of the entry's item.

## Behavior

- V: finds the row's parts by name: 'NameEquip' (text), 'IconEquip' (image), a count text whose name the list's virtual +96 returns, 'NumEquipB' (text) and an image whose name the virtual +88 returns.
- V: icon and name: ItemCell_SetItem(list + 24, {IconEquip, NameEquip or a text control, ...}, entry->itemId, 0).
- V: with nameTextId > 0 the name is formatted into NameEquip through UI text nameTextId; otherwise NameEquip receives the name directly.
- V: the +96 text shows entry +12 (equipped count), 'NumEquipB' entry +16 (owned count), with the UI text ids at list +1328 / +1332.
- V: the +88 image gets state (dword at Item-en row +36) + 1 from UITable_GetRowByKey(45, itemId); nothing when the row is missing.

## State touched

- Calls: [ItemCell_SetItem](ItemCell_SetItem.md), [UITable_GetRowByKey](UITable_GetRowByKey.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [UIName_Key](UIName_Key.md)
- Reads: [ShopEntry.item_id](../structs/ShopEntry.md#item_id)

## Referenced by

- Called by: [ShopItemList_DrawRow](ShopItemList_DrawRow.md), [sub_1402A6710](sub_1402A6710.md)
- Observed behaviours: [ItemDisplayInShopAndEquipPanels](../behaviors/ItemDisplayInShopAndEquipPanels.md)

## Notes

The name, the icon and the category image all come from the item id: an id without an Item-en row or without icon files shows nothing new in these parts.

## Open questions

I: the +36 column is the UI item category; ? the two parts the virtual names select.
