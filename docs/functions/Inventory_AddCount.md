# Inventory_AddCount

- **Address:** `0x1402847F8`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Inventory_AddCount(uint16_t id, int delta)`
- **Callers:** 32 direct sites in 21 functions: Item_CountTotal, sub_1402875A4, sub_140288590, sub_1402888E8, Party_ReturnHandItems, Inventory_BuildEquipList, sub_14028916C, sub_1402D65D4, sub_1403331F8, sub_140333640, sub_140333884, sub_140334208, sub_140334A48, sub_1403358FC, sub_140336664, JobChange_FillUnitEntry, sub_14036B71C, sub_14036C874, sub_1403931F0, sub_1403934B0 and sub_140396D08
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds a signed delta to the owned count of one item id and returns the new count, or zero when the id is outside the accepted range.

## Behavior

- V: the id argument is masked to ten bits (0x3FF) before the range test, so only the low ten bits of the id reach the count array.
- V: the range test accepts ids 1 through 260 and rejects 0 and everything above 260 ((id - 1) > 0x103).
- V: count = byte_1411A7C00[id] + delta, clamped below at 0 rather than wrapping, stored as a byte and returned.
- V: there is no upper clamp here; the callers cap at 99.
- V: it is a leaf: it calls nothing and reads only the count array (one rip-relative operand) and its own arguments.
- V: 32 direct call sites in 21 functions, including the menu list builder, the shop handler and the equip-preview code, which makes it the single write point for counts in most of the item path.
- I: the clamp-at-zero behaviour is what makes a negative delta safe for a sell or a use; the 99 cap is enforced by the callers, not here.
- I: the 10-bit mask is not redundant with the bound: callers pass packed words such as the party hand word (bit 15 = slot present), and the mask strips those flag bits before the id is used.

## State touched

- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Referenced by

- Called by: [ClassicItemUsePage_Run](ClassicItemUsePage_Run.md), [Inventory_BuildEquipList](Inventory_BuildEquipList.md), [Item_CountTotal](Item_CountTotal.md), [JobChange_FillUnitEntry](JobChange_FillUnitEntry.md), [Party_ReturnHandItems](Party_ReturnHandItems.md), [sub_1402875A4](sub_1402875A4.md), [sub_140288590](sub_140288590.md), [sub_1402888E8](sub_1402888E8.md), [sub_14028916C](sub_14028916C.md), [sub_1402D65D4](sub_1402D65D4.md), [sub_1403331F8](sub_1403331F8.md), [sub_140334A48](sub_140334A48.md), [sub_1403358FC](sub_1403358FC.md), [sub_140336664](sub_140336664.md), [sub_14036B71C](sub_14036B71C.md), [sub_140396D08](sub_140396D08.md)

## Notes

- V: leaf function; the whole body was read.

## Open questions

None recorded.
