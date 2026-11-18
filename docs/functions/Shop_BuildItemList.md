# Shop_BuildItemList

- **Address:** `0x140288E54`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Shop_BuildItemList(unsigned short unit, short shop, unsigned short category, unsigned short *out, int mode, int sort)`
- **Callers:** sub_140287D9C, sub_1402D7640, sub_14036A9D8, sub_14036C3EC, sub_14036E5DC
- **Callees:** EventVar_Read, `sub_1402890C0` (Item_MenuCategory), Item_GetRecord, Item_CanUnitEquip, PoachersDen_AddStock, `sub_140285B10`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the item id list of one shop or of the Poachers' Den into a caller-supplied buffer, applying the shop mask, the
story-progress gate, a menu-category filter and an optional equipment check, and returns the number of ids written.

## Behavior

- V: the first argument is the unit used by the equipment check, the second is the shop number, the third selects the menu
  category, the fourth is the output buffer, and the fifth and sixth are the mode and sort flags passed on the stack.
- V: shop numbers 0 through 14 take the town-shop branch; 15 through 99 produce an empty list; 100 and above take the
  Poachers' Den branch.
- V: in the town branch, the story-progress value is read once from event variable 111 and each candidate item is skipped
  when the byte at offset 10 of its record is larger than that value.
- V: in the town branch, the shop mask is two bytes per item id at 0x14067F890, first byte high, combined as a 16-bit word;
  shop s is present when bit (0x8000 shifted right by s) is set. Shop 0 is the high bit of the first byte.
- V: in the den branch, the mask and the progress byte are not consulted; an id is listed when PoachersDen_AddStock called
  with a zero delta returns a non-zero count. The menu-category filter and the equip check still apply.
- V: the menu-category filter compares Item_MenuCategory of the id against a pair derived from the category argument: 0 or 1
  accept categories 0 and 1, 2 accepts 2, 3 accepts 3, 4 accepts 4, 5 accepts 0, 6 accepts 1 and 7 accepts 5.
- V: mode 2 keeps only items the unit can equip; mode 1 keeps every item but sets the 0x4000 bit on ids the unit cannot
  equip; mode 0 performs no equipment check.
- V: each accepted id is appended as a 16-bit word and the list is terminated with 0xFFFF after the last one; the
  terminator is an all-ones register stored as a word, so the literal 0xFFFF is not in the immediate stream.
- V: when the sort flag is non-zero the finished list is reordered by `sub_140285B10` with order group 6.
- V: the function performs no bound check on the output pointer; the count grows only with the number of accepted ids.
- V: the town loop visits ids 0 through 255 and the den loop visits ids 0 through 260 in the pristine code.
- V: the shop mask table lives in read-only data and nothing in the image writes it.
- V: the 0x4000 bit travels with the id in the same word, so the list entry is a packed id-plus-flag value rather than a
  bare id (the OR is at 0x140288FBD and 0x140289061, and the word is stored at 0x140288FC4 and 0x140289068).
- ?: why shop numbers between 15 and 99 exist; no caller passes one and they do not fall into the den branch.
- V: the cannot-equip bit is written by both list loops: the constant 0x4000 is loaded at 0x140288F12 (town) and 0x140288FF5 (den), ORed into the id at 0x140288FBD and 0x140289061, and the 16-bit word is stored at 0x140288FC4 and 0x140289068. The bit travels with the id because the store is a plain word write.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [sub_1402890C0](sub_1402890C0.md), [Item_GetRecord](Item_GetRecord.md), [Item_CanUnitEquip](Item_CanUnitEquip.md), [PoachersDen_AddStock](PoachersDen_AddStock.md), [sub_140285B10](sub_140285B10.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [ItemRecord.shop_progress](../structs/ItemRecord.md#shop_progress), [g_MenuList](../globals/g_MenuList.md)
- Writes: [MenuListWord.cannot_equip](../structs/MenuListWord.md#cannot_equip), [MenuListWord.item_id](../structs/MenuListWord.md#item_id)

## Referenced by

- Appears in flows: [ItemMenuListLifecycle](../flows/ItemMenuListLifecycle.md)
- Called by: [sub_140287D9C](sub_140287D9C.md), [sub_1402D7640](sub_1402D7640.md), [sub_14036A9D8](sub_14036A9D8.md), [sub_14036C3EC](sub_14036C3EC.md), [sub_14036E5DC](sub_14036E5DC.md)
- Observed behaviours: [EquipListsDropRowsAUnitCannotEquip](../behaviors/EquipListsDropRowsAUnitCannotEquip.md), [ItemMenuListWordMarkOverlapsLargeIds](../behaviors/ItemMenuListWordMarkOverlapsLargeIds.md), [MenuListFlagFlow](../behaviors/MenuListFlagFlow.md)
- Reads tables: [ItemShopMask](../tables/ItemShopMask.md)

## Notes

- Only the shop-mask reads were studied in the first sheet; the loop bounds, the category pairs and the two equipment
  modes were added from the second read.

## Open questions

- ?: the meaning of the mask bit for shop slot 15, which no reader of the three that exist ever tests.
