# MenuListWord

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of g_MenuList, the array the shop, equip, item and ability screens reuse: the id in bits 0..9, bit 14 "cannot equip / cannot learn / current", and the list-kind-specific bits 12 and 13. 0xFFFF ends the list. Bit 15 is not written to this array by any producer.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="item_id"></a>bits 0..9 | item_id | `uint16` | V | Item, job or ability id. Fourteen of the functions that read the array mask it with 0x3FF; five pass or compare the whole word (sub_140334A48, sub_14036AC74, sub_14036C468, sub_1403331F8, sub_140285F2C). | [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md), [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [sub_140286A78](../functions/sub_140286A78.md), [sub_140366FE0](../functions/sub_140366FE0.md) | [ItemOrder_FilterList](../functions/ItemOrder_FilterList.md), [ShopEntry_InitFromList](../functions/ShopEntry_InitFromList.md), [sub_140285B10](../functions/sub_140285B10.md), [sub_140285F2C](../functions/sub_140285F2C.md), [sub_140286228](../functions/sub_140286228.md), [sub_140332C54](../functions/sub_140332C54.md), [sub_140332C8C](../functions/sub_140332C8C.md), [sub_140332CD0](../functions/sub_140332CD0.md), [sub_140332D48](../functions/sub_140332D48.md), [sub_140333974](../functions/sub_140333974.md), [sub_140334A48](../functions/sub_140334A48.md), [sub_140366FE0](../functions/sub_140366FE0.md), [sub_14036A994](../functions/sub_14036A994.md), [sub_14036AC74](../functions/sub_14036AC74.md), [sub_14036C468](../functions/sub_14036C468.md) |
| <a id="flag_0x1000"></a>bit 12 | flag_0x1000 | `bit` | V | Ability list only: JobAbilityList_Build mode 2 ORs 0x1000 into an already-known ability (0x140286A03); sub_14028A474 also ORs 0x1000 into an ability row. No reader of this bit was found. | [JobAbilityList_Build](../functions/JobAbilityList_Build.md) |  |
| <a id="flag_0x2000"></a>bit 13 | flag_0x2000 | `bit` | V | Ability list only: JobAbilityList_Build mode 0 combines it with bit 14 (0x6000) for an ability hidden from the tree (0x140286A25). The job list uses the same bit for a locked job. | [JobAbilityList_Build](../functions/JobAbilityList_Build.md) |  |
| <a id="cannot_equip"></a>bit 14 | cannot_equip | `bit` | V | Cannot equip (shop and equip list; 0x140288FBD, 0x140288CAF), cannot learn (ability list; 0x1402869F3, 0x140286B81), or current job (g_RuntimeJobList only). Seven functions test it: ShopEntry_Fill, sub_140332C54, sub_140332C8C, sub_140336664, sub_14036A994, sub_140366FE0, sub_140333974. | [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md), [JobAbilityList_Build](../functions/JobAbilityList_Build.md), [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [sub_140286A78](../functions/sub_140286A78.md) | [ItemOrder_FilterList](../functions/ItemOrder_FilterList.md), [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [sub_140286228](../functions/sub_140286228.md), [sub_140332C54](../functions/sub_140332C54.md), [sub_140332C8C](../functions/sub_140332C8C.md), [sub_140333974](../functions/sub_140333974.md), [sub_140336664](../functions/sub_140336664.md), [sub_140366FE0](../functions/sub_140366FE0.md), [sub_14036A994](../functions/sub_14036A994.md) |
| <a id="not_current_equipment"></a>bit 15 | not_current_equipment | `bit` | V | Not set on g_MenuList. The only function that sets it is sub_140287D9C (0x140288544), on its four-word output buffer (g_EquipCandidates), not on this array; sub_1402875A4 has no 0x8000 immediate, and no g_MenuList reader tests bit 15. |  |  |
| <a id="terminator"></a>list end | terminator | `uint16` | V | Ends the list; this array uses 0xFFFF, unlike the ten saved order lists, which end at 0xFF. |  |  |

## Behavior

- V: the same 256-word array is reused by four list kinds: shop (Shop_BuildItemList), equip (Inventory_BuildEquipList), ability (JobAbilityList_Build, sub_140286A78) and item/equip pages (sub_14036C3EC).
- V: 31 exported functions hold 49 instructions that name the array: 41 load its address with lea (as an output list or a callee argument) and 8 read an entry directly.
- V: a builder stops at 145 entries and writes the 0xFFFF terminator; the insert path of the sorter stops at 146.
- V: the array is rebuilt whenever a screen opens and is never saved, but sub_140285F2C copies its words into the saved order list off_14067F498[group] and sub_140336B88 copies a stack list into off_14067FA90, both without stripping flag bits.

## Referenced by

- Observed behaviours: [ItemMenuListWordMarkOverlapsLargeIds](../behaviors/ItemMenuListWordMarkOverlapsLargeIds.md), [MenuListFlagFlow](../behaviors/MenuListFlagFlow.md)

## Notes

V: the sheets of the builders, the row helpers and the two movers.

## Open questions

? who reads bit 12 or bit 13 of an ability entry; ? whether a flagged word can reach off_14067F498 through sub_140285F2C in a running screen (the one caller builds the list in mode 0, so no flagged word was seen on that path).
