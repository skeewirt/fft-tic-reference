# ItemIdSpace

- **Kind:** observed behaviour
- **Scope:** the item functions and every bound on an item id
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [Item_GetRecord](../functions/Item_GetRecord.md), [Item_FindCategoryIndex](../functions/Item_FindCategoryIndex.md), [Item_IsValidId](../functions/Item_IsValidId.md), [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [g_ItemNewFlags](../globals/g_ItemNewFlags.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Item ids are u16 wherever they are stored for units (roster, party, battle and preview records), but the code bounds them in three ways: the item functions serve 0..0x104 (two stock record arrays split at 0x100), about 39 code sites compare an id with 0x105 (or 0x104 / 0x103) before using it, and several stores have exactly 261 entries (inventory, Poachers' Den, new flags, item order lists). Menu and battle paths mask ids with 0x1FF or 0x3FF.

## Behavior

- V: ItemIcon_Set (item icons) takes ids below 0x200; the hand-slot readers of the unit panels mask with 0x1FF, the menus with 0x3FF; bit 14 (0x4000) of a menu list entry marks an item the unit cannot equip.
- V: the menus list only items present in the saved item order lists (ItemOrder_FilterList drops the others); those lists are filled for ids 1..260 by ItemOrder_SyncGroup and have fixed capacities.
- V: five display functions derive the 255 empty-slot sentinel from the 0x105 bound register (bound minus 6).

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
