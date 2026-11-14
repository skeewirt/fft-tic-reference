# EquipDetail_SetHelpText

- **Address:** `0x1402A0A08`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void EquipDetail_SetHelpText(EquipDetail *panel, ItemRef *item, int line)`
- **Callers:** EquipDetail_Refresh
- **Callees:** ItemTable_GetRow, Item_GetRecord, Item_GetWeaponRecord, sub_1402A0E58, GUITextNode_SetTextExpandedTemp, GUINode_ApplyStateAtFrame

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes one help line of the equipment detail panel: line 0 = the item's description from Item-en, line 1 = three lines built by sub_1402A0E58, line 2 = weapon notes.

## Behavior

- V: line 0: ItemTable_GetRow(item +0); returns without touching the text when the row is missing, else the string at row +16 (relative to row +4) goes into the line's text node.
- V: line 2 (item +8 != 5): for a record with slot bit 0x80 and a weapon record, UI texts 934, or 923 / 3812 and 924 / 3813 by weapon flag bits, are appended.
- V: an empty line shows UI text 917; 'ShowJobIcon' / 'HideJobIcon' follows line 2.

## State touched

- Calls: [ItemTable_GetRow](ItemTable_GetRow.md), [Item_GetRecord](Item_GetRecord.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md)

## Referenced by

- Observed behaviours: [ItemDisplayInShopAndEquipPanels](../behaviors/ItemDisplayInShopAndEquipPanels.md)

## Notes

With no Item-en row the description node keeps the previous item's text (V: the early return; I: that is why item 300 showed the Rod's description).

## Open questions

? what item +8 == 5 means here; the callers pass different item structs (the shop passes its 40-byte entry).
