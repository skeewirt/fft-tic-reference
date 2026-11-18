# ItemMenuListLifecycle

- **Kind:** flow
- **Area:** [Items and shops](../areas/items.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where a shop or equip list word is written, reordered and read: one producer fills g_MenuList for the screen, the saved-order filter rewrites it right after a mode-1 build, and seven functions read single words back, three of them to get the item id and the 'cannot equip' mark.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [Shop_BuildItemList](../functions/Shop_BuildItemList.md) | V | Town loop and Poachers' Den loop: each accepted id is stored as one word; in mode 1 an id the unit cannot equip gets 0x4000 ORed in first (constant loaded at 0x140288F12 and 0x140288FF5, stores at 0x140288FC4 and 0x140289068). The mark is set only with a unit and mode 1. |
| <a id="2"></a>2 | [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md) | V | Equip list: the same mark through a bit-set of bit 14 at 0x140288CAF, stored at 0x140288CB6, mode 1 only; modes 2 and above drop the refused id instead and mode 0 never asks. |
| <a id="3"></a>3 | [ItemOrder_FilterList](../functions/ItemOrder_FilterList.md) | V | Called by the screens' list builders right after a mode-1 build (ShopList_BuildEntries at 0x14036B1EB, sub_1403368C0 at 0x14033695A) and by Inventory_BuildEquipList itself for the order-list groups: it rewrites g_MenuList in the saved order and drops the ids that order does not name, so the position of a word in the list changes after the producers have stored it. |
| <a id="4"></a>4 | [ShopEntry_Fill](../functions/ShopEntry_Fill.md) | V | Reads the list word of each displayed row; the word only feeds the entry's cannot-equip byte (shift by 14, AND 1). Mark only. |
| <a id="5"></a>5 | [sub_140332C54](../functions/sub_140332C54.md) | V | Row count: masks the word to an id for Item_CountTotal, then tests bit 14 afterwards. Id and mark. |
| <a id="6"></a>6 | [sub_140332C8C](../functions/sub_140332C8C.md) | V | Equipped count: the same shape, an AND with 0x4000 afterwards. Id and mark. |
| <a id="7"></a>7 | [sub_14036A994](../functions/sub_14036A994.md) | V | Price: the same shape with Item_GetRecord. Id and mark. |
| <a id="8"></a>8 | [sub_140336664](../functions/sub_140336664.md) | V | Memory test of 0x4000 on a list word, then a branch. Mark only. |
| <a id="9"></a>9 | [sub_140333974](../functions/sub_140333974.md) | V | Memory test of 0x4000 on a list word at 0x140333C5D, then a branch. Mark only. |
| <a id="10"></a>10 | [sub_140366FE0](../functions/sub_140366FE0.md) | V | Ability popup: a bit-14 test (0x14036732C) whose register is not used afterwards; on an ability list the bit means 'cannot learn', so this reader never sees an item. |

## Behavior

- V: the three writers are the only item producers of g_MenuList (Shop_BuildItemList twice, Inventory_BuildEquipList once); nothing reads the word between the instruction that sets the mark and the store.
- V: the seven readers are the functions that test bit 14 of a list word (the list above, steps 4 to 10); a scan of the 127 functions that call an item helper (Item_GetRecord, Item_CountTotal, Item_MenuCategory, Item_CanUnitEquip, Inventory_AddCount, Item_CountEquippedByParty, Item_SellPrice, Item_IsValidId) found no other bit-14 or bit-15 test on an item list word; the rest of the hits are random numbers, button masks and a battle message flag on a byte id.
- I: a possession-list word (0x141D32F00) has two readers that test 0x4000 and a Classic item-use page; by static callers they are reached only from the Classic item pages (ClassicItemUsePage_Run, ClassicItemListPage_Run and two helpers, entered from data tables), so no Enhanced screen reaches them by a direct call.

## Notes

Word layout and the overlap of the mark with a 15-bit id: ItemMenuListWordMarkOverlapsLargeIds.

## Open questions

? which of the callers of Inventory_BuildEquipList and Shop_BuildItemList pass mode 1 and which pass mode 2 (the mode is a stack argument built from a variable at most call sites).
