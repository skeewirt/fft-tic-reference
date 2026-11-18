# ItemOrder_FilterList

- **Address:** `0x140285DF0`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int ItemOrder_FilterList(uint16_t *orderList, uint16_t *list)`
- **Callers:** sub_140286228, Inventory_BuildEquipList, sub_1403368C0, sub_140338250, ShopList_BuildEntries (five direct sites)
- **Callees:** memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reorders a 0xFFFF-terminated item list by a saved order list, dropping every entry the order list does not name. The list is filtered in place; the return value is the number of entries kept.

## Behavior

- V: takes the saved order list in the first argument and the display list in the second; both are arrays of 16-bit words.
- V: reads the order list until it meets the value 255 or any value of 261 or above (0x105); both end the scan.
- V: for each order entry it walks the display list from the start and compares against the entry's low ten bits (0x3FF), so the flag bit carried by display entries is ignored for matching.
- V: on a match it copies the display entry unchanged (flag bit included) into a stack buffer at rsp+0x20.
- V: after the last order entry it writes the 65535 terminator into the buffer and copies the buffer back over the display list with memmove, two bytes per entry plus the terminator.
- V: entries of the display list that no order entry names are lost.
- V: there is no capacity check on the order list; the stack buffer covers the largest display list (256 words) plus a terminator.
- V: the copy is followed by the compiler's stack-cookie check.
- I: both the shop list builder and the equipment list builder call it, so the saved user order is the single ordering rule for those screens.
- ?: whether a display entry with the flag bit set is ever meant to sort differently from the same id without it.
- V: the order id is compared unmasked with the list word masked by 0x3FF (constant at 0x140285E5E, mask at 0x140285E63); a match copies the whole list word to a stack buffer at 0x140285E7E, and the buffer is moved back with memmove at 0x140285EA8. Flags travel, and a flagged order id never matches.
- V: it runs on g_MenuList right after the mode-1 builds of `ShopList_BuildEntries` (call site 0x14036B1EB lies in that caller, not in this function) and `sub_1403368C0` (call site 0x14033695A, also in the caller), so the order of the list after the producers is the saved order, not the build order (flow ItemMenuListLifecycle).

## State touched

- Reads: [MenuListWord.item_id](../structs/MenuListWord.md#item_id), [MenuListWord.cannot_equip](../structs/MenuListWord.md#cannot_equip)

## Referenced by

- Appears in flows: [ItemMenuListLifecycle](../flows/ItemMenuListLifecycle.md)
- Called by: [Inventory_BuildEquipList](Inventory_BuildEquipList.md), [ShopList_BuildEntries](ShopList_BuildEntries.md), [sub_140286228](sub_140286228.md), [sub_1403368C0](sub_1403368C0.md), [sub_140338250](sub_140338250.md)
- Observed behaviours: [OrderInsideItemGroup](../behaviors/OrderInsideItemGroup.md)

## Notes

- V: the whole body was read.

## Open questions

None recorded.
