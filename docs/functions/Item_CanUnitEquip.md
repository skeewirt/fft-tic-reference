# Item_CanUnitEquip

- **Address:** `0x1402886D0`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Item_CanUnitEquip(unsigned short id, short job, void *equipFlags)`
- **Callers:** `Inventory_BuildEquipList`, `Shop_BuildItemList` (two sites), `UnitWork_BuildForSlot`, `sub_140288788`, `sub_1402C20F0`, `sub_14036AC38` (six functions, seven sites)
- **Callees:** `sub_1402890C0` (Item_MenuCategory), `Item_GetRecord`, `BitReader_ReadBits`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether a unit's job may equip an item, combining the job's equip-category bits with a small set of item ids the
game special-cases.

## Behavior

- V: The item id is masked to ten bits, and a zero id returns 1 (true) immediately, not false.
- V: The job id is sign-extended from 16 bits and kept for the special-id test.
- V: The function first asks the menu-category helper for the id; menu category 5 returns -1 (false).
- V: The unmasked ids 262, 288, 293, 301 and 310 are reached as a chain of subtractions from 0x106, then 0x1A, 5, 8 and a
  compare with 9; each of them returns 1 only for jobs 161 and 164, and -1 for every other job.
- V: The generic path reads the item record's byte at +5 (equip_category) as a bit index and reads one bit from the stream
  passed in the third argument through the bit reader; the bit set gives 1 and the bit clear gives -1.
- V: The two outcomes are 1 and -1 (the failure value is produced as all-ones), not 0 and 1.
- V: Six direct callers reach it over seven call sites, and it calls the category lookup, the record accessor and the bit
  reader.
- I: The two job ids are almost certainly the two special jobs that may equip the reserved items, but the code does not
  name them.
- I: The five special ids lie past the stock items (0..260) and are leftovers of a larger item list; Item_CanUnitEquipPreview
  applies the same test.

## State touched

- Calls: [sub_1402890C0](sub_1402890C0.md), [Item_GetRecord](Item_GetRecord.md)
- Reads: [ItemRecord.equip_category](../structs/ItemRecord.md#equip_category)

## Referenced by

- Called by: [Inventory_BuildEquipList](Inventory_BuildEquipList.md), [Shop_BuildItemList](Shop_BuildItemList.md), [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md), [sub_140288788](sub_140288788.md), [sub_1402C20F0](sub_1402C20F0.md)

## Notes

- I: This is the function the item takeover has to keep data-driven if the reserved-id special case is to survive.

## Open questions

None recorded.
