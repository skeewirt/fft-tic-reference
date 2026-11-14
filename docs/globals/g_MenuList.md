# g_MenuList

- **Kind:** global
- **Address:** `0x141811470`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint16[256]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The display list shared by the shop and the equip screens: up to 256 packed words, 0xFFFF-terminated, rebuilt whenever a screen opens and never saved. It is one array, not one per screen.

## Behavior

- V: four builders pass this address as Inventory_BuildEquipList's output list: sub_1403368C0, sub_140336B88, sub_140338250 and sub_140334A48; Shop_BuildItemList, JobAbilityList_Build and sub_140286A78 also write it for the shop and ability lists.
- V: 31 exported functions hold 49 instructions that name the array: 41 load its address with lea and 8 read an entry directly; ShopEntry_Fill reads it directly for each displayed row.
- V: the builders stop at 145 entries and write the 0xFFFF terminator, and the order sorter's insert scan stops at 146, so the array is larger than any list a stock builder produces.
- V: the order lists are filters over this list, not copies of it: each screen rebuilds it and then either rewrites it in place or filters it through a saved list. The exception is sub_140285F2C, which copies its words into the saved order list off_14067F498[group].

## Referenced by

- Observed behaviours: [MenuListFlagFlow](../behaviors/MenuListFlagFlow.md), [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md)
- Read by: [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [sub_140285F2C](../functions/sub_140285F2C.md), [sub_140332C54](../functions/sub_140332C54.md), [sub_140332C8C](../functions/sub_140332C8C.md), [sub_140332CD0](../functions/sub_140332CD0.md), [sub_140332D48](../functions/sub_140332D48.md), [sub_140333974](../functions/sub_140333974.md), [sub_140334A48](../functions/sub_140334A48.md), [sub_140335604](../functions/sub_140335604.md), [sub_1403358FC](../functions/sub_1403358FC.md), [sub_140336444](../functions/sub_140336444.md), [sub_140336664](../functions/sub_140336664.md), [sub_1403368C0](../functions/sub_1403368C0.md), [sub_140336B88](../functions/sub_140336B88.md), [sub_140338250](../functions/sub_140338250.md), [sub_140366FE0](../functions/sub_140366FE0.md), [sub_14036A924](../functions/sub_14036A924.md), [sub_14036A95C](../functions/sub_14036A95C.md), [sub_14036A994](../functions/sub_14036A994.md), [sub_14036AC74](../functions/sub_14036AC74.md), [sub_14036B5D0](../functions/sub_14036B5D0.md), [sub_14036C468](../functions/sub_14036C468.md)
- Written by: [sub_140286A78](../functions/sub_140286A78.md), [sub_1402D7640](../functions/sub_1402D7640.md), [sub_140333974](../functions/sub_140333974.md), [sub_140334A48](../functions/sub_140334A48.md), [sub_1403368C0](../functions/sub_1403368C0.md), [sub_140336B88](../functions/sub_140336B88.md), [sub_140338250](../functions/sub_140338250.md), [sub_14036A9D8](../functions/sub_14036A9D8.md), [sub_14036B5D0](../functions/sub_14036B5D0.md), [sub_14036C3EC](../functions/sub_14036C3EC.md), [sub_14036C49C](../functions/sub_14036C49C.md), [sub_14036E5DC](../functions/sub_14036E5DC.md)

## Notes

V: the sheets of the builders, ShopEntry_Fill, sub_140285F2C and sub_140336B88.

## Open questions

? whether a flagged word ever reaches off_14067F498 through sub_140285F2C (its one caller builds the list in mode 0, so none was seen) and who reads bit 12 or 13 of an ability entry.
