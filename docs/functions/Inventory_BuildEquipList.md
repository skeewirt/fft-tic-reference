# Inventory_BuildEquipList

- **Address:** `0x140288B94`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int Inventory_BuildEquipList(int16_t unit, int16_t sortWord, char group, uint16_t *out, int unused, uint8_t mode)`
- **Callers:** sub_1402875A4, sub_140333974, sub_140334A48, sub_1403368C0, sub_140336B88 (twice), sub_140338250, sub_14036C3EC (seven functions)
- **Callees:** Inventory_AddCount, Item_CountTotal, `sub_1402890C0` (Item_MenuCategory), Item_CanUnitEquip, `sub_140285B10`, ItemOrder_FilterList

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the candidate list of items a unit may take from one menu group, in id order, and then orders that list either by
a sort field or by the saved user order. It is the one producer of the shared menu list that the equipment and shop screens
display.

## Behavior

- V: scans item ids from 1 up to 260 (the loop bound is 0x105) in ascending order.
- V: drops an id whose count is zero; the count comes from the mode byte: mode 3 reads the inventory count alone through
  Inventory_AddCount with a zero delta, every other mode reads owned plus equipped through Item_CountTotal.
- V: keeps an id only when its menu category matches the group argument. The hand group accepts two categories (0 and 1);
  groups 2, 3, 4, 5, 6 and 7 map to categories 2, 3, 4, 0, 1 and 5, so six further groups map to one category each.
- V: asks the equip check whether the given unit may equip the id; the job comes from the unit record's word at +0x24 and
  the equip flags from byte 0x73 of the same record.
- V: in mode 1 a refused item is kept and marked with bit 14 of its list word; the bit is set as bit 0xE, so the literal
  0x4000 does not appear as an immediate. In mode 2 and above the refused item is dropped, and mode 0 performs no equip
  check.
- V: stops at 145 entries and writes the 0xFFFF terminator after the last one; the terminator is produced as an all-ones
  register and stored as a word, so the literal 0xFFFF is not in the immediate stream.
- V: after the build the second word argument decides the order: zero keeps the id order as built, a value from 1 to 5
  filters the list through one of the saved order lists at 0x14067F498 (the index is derived from the group) and drops the
  entries the list does not name, and any other value sorts it with `sub_140285B10` using the argument's low four bits as
  the sorter group.
- V: the fifth declared argument is never read by this function, and the call sites examined do not write it, so only five
  arguments carry data; the mode byte is the sixth stack argument.
- V: the second word argument is stored at entry and read again after the build as the order selector.
- I: the equipment screen and the item menu call it, which is why the same 145-entry cap and the same output array appear in
  both.
- ?: what the unused fifth argument was meant to carry.
- V: in mode 1 a refused item gets bit 14 through the bit-set at 0x140288CAF and is stored with the id at 0x140288CB6; modes 2 and 3 drop the item instead, and mode 0 never tests it.
- V (seen live): the Fitting list and the Status equipment list show no row for an item the unit cannot equip; the mark of mode 1 is not drawn as a greyed row there (behavior EquipListsDropRowsAUnitCannotEquip, flow ItemMenuListLifecycle).

## State touched

- Calls: [Inventory_AddCount](Inventory_AddCount.md), [Item_CountTotal](Item_CountTotal.md), [sub_1402890C0](sub_1402890C0.md), [Item_CanUnitEquip](Item_CanUnitEquip.md), [sub_140285B10](sub_140285B10.md), [ItemOrder_FilterList](ItemOrder_FilterList.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md)
- Writes: [MenuListWord.cannot_equip](../structs/MenuListWord.md#cannot_equip), [MenuListWord.item_id](../structs/MenuListWord.md#item_id)

## Referenced by

- Appears in flows: [ItemMenuListLifecycle](../flows/ItemMenuListLifecycle.md)
- Called by: [sub_1402875A4](sub_1402875A4.md), [sub_140333974](sub_140333974.md), [sub_140334A48](sub_140334A48.md), [sub_1403368C0](sub_1403368C0.md), [sub_140336B88](sub_140336B88.md), [sub_140338250](sub_140338250.md), [sub_14036C3EC](sub_14036C3EC.md)
- Observed behaviours: [EquipListsDropRowsAUnitCannotEquip](../behaviors/EquipListsDropRowsAUnitCannotEquip.md), [ItemMenuListWordMarkOverlapsLargeIds](../behaviors/ItemMenuListWordMarkOverlapsLargeIds.md), [MenuListFlagFlow](../behaviors/MenuListFlagFlow.md), [OrderInsideItemGroup](../behaviors/OrderInsideItemGroup.md)

## Notes

Read end to end (466 bytes); the category mapping was cross-checked against the item category table. The post-build branch
was re-read from the bytes for this merge: the order selector is the second word argument, not the fifth.

## Open questions

None recorded.
