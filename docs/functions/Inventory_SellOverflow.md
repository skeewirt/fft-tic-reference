# Inventory_SellOverflow

- **Address:** `0x1402846C0`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `bool Inventory_SellOverflow(void)`
- **Callers:** sub_1402EEE30 (one direct site)
- **Callees:** Item_CountTotal, Item_SellPrice, sub_140284684, sub_140288590, __report_rangecheckfailure

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sells down every inventory count above 99 and adds the gil, which is the overflow rule the rest of the item path relies on.

## Behavior

- V: one loop walks the inventory from id 1 while the id is below 261 (0x105), calling Item_CountTotal for each one; there is no second walk.
- V: for a total of 100 or more it computes over = total - 99, adds over * Item_SellPrice(id) gil and writes the capped count back.
- V: when the inventory byte itself is below over, the count is set to 0 and the item is unequipped from the party member whose byte +0x175 (373) is highest among those wearing it in the five hand words +84..+92; sub_140288590 does the removal (unit index, slot, 0).
- V: returns whether anything was sold (the byte in al).
- V: the index is range-checked against 0x105 before the write, with a call to __report_rangecheckfailure on the failure path.
- I: because the loop bound and the array size are the same 261, this function is one of the places where growing the item space without moving the array would read past it.

## State touched

- Calls: [Item_CountTotal](Item_CountTotal.md), [Item_SellPrice](Item_SellPrice.md), [sub_140288590](sub_140288590.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Notes

- I: the 99 cap is a game rule carried in the code, not a width; it is separate from the 261 id bound.
- V: four helper calls plus the compiler's bounds trap; the earlier note of a second loop and eight helpers is not in the bytes.

## Open questions

None recorded.
