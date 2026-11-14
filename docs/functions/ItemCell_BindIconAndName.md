# ItemCell_BindIconAndName

- **Address:** `0x14029BEC4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ItemCell_BindIconAndName(void *ctx, ItemCellParts *parts, int itemId, const char *iconPath, char showEmpty)`
- **Callers:** ItemCell_SetItem (sub_14029ADE4), EquipDetail_Refresh
- **Callees:** ItemTable_GetName (sub_1402B892C), JobTreePanel_SetTextKey, sub_14002620C, FormatArgs_Push, sub_14028F754

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds an item's icon image and name text to a cell's parts; a missing Item-en row leaves both unset.

## Behavior

- V: the name is ItemTable_GetName(itemId); the cell is 'set' when the name exists and itemId >= 0.
- V: when itemId != 0 or showEmpty: with a third part (parts[2]) the icon goes to parts[0] and the name into the third part's text arguments; without it JobTreePanel_SetTextKey binds the icon path to parts[0] and the name to parts[1].
- V: writes the 'set' flag (0 or 1) to byte +144 of parts[0] and parts[1]; with itemId 0 and no showEmpty the flag is 0.

## State touched

- Calls: [ItemTable_GetName](ItemTable_GetName.md), [JobTreePanel_SetTextKey](JobTreePanel_SetTextKey.md), [sub_14002620C](sub_14002620C.md), [FormatArgs_Push](FormatArgs_Push.md)

## Referenced by

- Appears in flows: [ItemNameToScreen](../flows/ItemNameToScreen.md)
- Called by: [EquipDetail_Refresh](EquipDetail_Refresh.md), [ItemCell_SetItem](ItemCell_SetItem.md)
- Observed behaviours: [ItemDisplayInShopAndEquipPanels](../behaviors/ItemDisplayInShopAndEquipPanels.md)

## Open questions

? what byte +144 of a GUI part controls (I: shown / hidden).
