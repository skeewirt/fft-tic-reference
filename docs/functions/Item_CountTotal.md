# Item_CountTotal

- **Address:** `0x140287530`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Item_CountTotal(uint16_t id)`
- **Callers:** 12 direct sites: sub_1401AFFC4, Inventory_SellOverflow, ItemOrder_SyncGroup, sub_140286070, sub_140286160, Inventory_BuildEquipList, sub_14028B354, ShopEntry_InitFromList, sub_140332C54, sub_140334A48, JobChange_FillUnitEntry and sub_14036A924
- **Callees:** Inventory_AddCount, Item_CountEquippedByParty

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns everything the party owns of an item: the inventory count plus the number equipped by the party.

## Behavior

- V: It masks the id to ten bits (0x3FF) once, then calls Inventory_AddCount with a delta of zero to read the inventory count.
- V: It passes the same masked id to Item_CountEquippedByParty and returns the sum.
- V: It calls exactly two functions and has twelve direct callers, including the shop rows and the item menu.
- I: Reading the count by calling the add helper with zero rather than a dedicated getter is the pattern the rest of the inventory code uses.

## State touched

- Calls: [Inventory_AddCount](Inventory_AddCount.md), [Item_CountEquippedByParty](Item_CountEquippedByParty.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Referenced by

- Called by: [Inventory_BuildEquipList](Inventory_BuildEquipList.md), [Inventory_SellOverflow](Inventory_SellOverflow.md), [ItemOrder_SyncGroup](ItemOrder_SyncGroup.md), [JobChange_FillUnitEntry](JobChange_FillUnitEntry.md), [ShopEntry_InitFromList](ShopEntry_InitFromList.md), [sub_140286070](sub_140286070.md), [sub_140286160](sub_140286160.md), [sub_14028B354](sub_14028B354.md), [sub_140332C54](sub_140332C54.md), [sub_140334A48](sub_140334A48.md), [sub_14036A924](sub_14036A924.md)

## Notes

- V: whole body read.

## Open questions

None recorded.
