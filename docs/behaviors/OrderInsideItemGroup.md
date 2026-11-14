# OrderInsideItemGroup

- **Kind:** observed behaviour
- **Scope:** the order of item ids inside one menu group (the item menu, the equip screen and the shop list)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [ItemOrderLists](../structs/ItemOrderLists.md), [ItemOrder_SyncGroup](../functions/ItemOrder_SyncGroup.md), [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md), [sub_140286228](../functions/sub_140286228.md), [sub_140285B10](../functions/sub_140285B10.md), [sub_14028B180](../functions/sub_14028B180.md), [sub_14028B354](../functions/sub_14028B354.md), [ItemOrder_FilterList](../functions/ItemOrder_FilterList.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Three rules decide the order, in this priority: the saved order list is the order, membership maintenance inserts a newly owned id at the front and removes a lost one, and an explicit sort replaces the order with a field-by-field comparison. The field schedules live in data; the key getter, the comparator and the two sorters are the only code that imposes an order.

## Behavior

- V: the saved list is the order. A consumer either copies the list or filters the menu list through it, so the output keeps the list's order and every id the list does not hold is dropped.
- V: membership maintenance inserts a newly owned id at index 0, removes an id that is no longer owned and leaves every other entry where it is; it never sorts.
- V: an explicit sort replaces the order. Modes 0..7 select byte lists of item record fields from the table at 0x14067FAB0, and the insertion sort swaps when the comparator's key difference is zero or more.
- V: the keys are the equipment category byte with 19 remapped to 100 (field 0), the price (1), a sub-record byte (2), two equipment bytes (3 and 4), the total owned plus equipped count (5), the name string (9), the id (10), a flag true for one chosen id (11) and the item text row's dword at +0x28, or 999999 when the row is missing (12); fields 6, 7 and 8 have no key.
- V: the obtain-order case is a filter, not a sort: field 8 first keeps only the ids the obtain-order list holds, then moves one chosen id to the front.
- V: the menu candidate builder caps its output at 145 ids and stops its id walk at 0x104; the order filter uses a 264-word stack buffer.
- V: swapping on an equal key makes the sort unstable: two ids with the same key exchange places instead of keeping their saved order.
- I: because the two screens keep independent lists (A for the item menu, B for the equip screen) the same item can sit at different positions in the two menus; no function reads both lists together.

## Notes

V: the three rules, the field table and the key table; the screens' names are labels taken from the builders and the UI state they read.

## Open questions

? the screen names: no string or scene id in the image names the item menu or the equip screen, so the labels are inferred from the builders and the UI state they read.
