# Unit_ListThrowableItems

- **Address:** `0x14030E7B4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Unit_ListThrowableItems(int unit_slot, uint8_t command, uint8_t *out)`
- **Callers:** sub_14023678C, sub_1402EA58C, sub_14030E174
- **Callees:** `sub_14030DB88`, `sub_14030E368`, `Item_GetRecord`, `sub_1402B8C74` (Item_GetWeaponRecord), `sub_1405DB690` (qsort), `__security_check_cookie`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the candidate list for the Throw command: the item ids in the unit's inventory that the game considers
throwable, ordered for the menu.

## Behavior

- V: the arguments are a battle unit slot, a command id and the caller's output buffer.
- V: it returns 0 when the unit slot has no live unit, and 0 when the command id is not 20.
- V: it calls `sub_14030E368` to build the command's usable ability list, then converts the throw abilities 382..393
  into the twelve equip-category bytes of the table at `0x140789290`; the table read is at 0x14030E886.
- V: it then scans item ids from 0 to 255 inclusive; an item numbered 256 or above is never examined.
- V: an item is kept only when its record's equip-category byte at +5 is one of those twelve values.
- V: an item is kept only when its record's slot-flags byte at +3 is signed-negative, which is the weapon-slot bit.
- V: an item is kept only when its weapon record's flag byte at +1 has bit 2 set.
- V: the stock test is skipped when the owning unit's team bits (record +0x1EE, mask `0x30`) are set: the set case jumps
  straight to the append, so an enemy unit lists a throwable even with a zero count, and only a unit with the bits clear
  needs a non-zero inventory count at `0x1411A7C00`.
- V: it writes each kept id as one byte and terminates the list with `0xFF` at the position the count points to.
- V: it returns the count as an 8-bit value, so a list of 256 entries would report zero.
- V: before returning it sorts the list with the standard sort routine `sub_1405DB690`, element size one.
- V: the comparator it passes (0x14030E774, handed to qsort, not called here) reads the two item ids, asks 0x1400F8674 for
  each one's row and orders them by the 32-bit field at row +0x28, ascending; both addresses belong to the comparator, not
  to this body.
- I: the twelve categories are the throwable weapon classes, because each maps one-to-one onto a Throw ability and
  items 122..127 are the six throwing weapons.
- I: weapon flag bit 2 is the stock "can be thrown" marker, because the six throwing weapons set it and no other
  weapon in the stock table does.
- V: the comparator is sub_14030E774 (Item_CompareSortOrder): it returns -1 / 0 / 1 from the Item row dword +0x28 (column sort_order; read in the comparator, not in this body), smaller first; sub_14030EEF0 uses it as well.
- I: sort_order is an order key, not a price: lists sorted by it place the smaller value first.

## State touched

- Calls: [sub_14030E368](sub_14030E368.md), [Item_GetRecord](Item_GetRecord.md), [sub_1402B8C74](sub_1402B8C74.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Referenced by

- Called by: [sub_14023678C](sub_14023678C.md), [sub_1402EA58C](sub_1402EA58C.md), [sub_14030E174](sub_14030E174.md)
- Observed behaviours: [ItemCommandRelation](../behaviors/ItemCommandRelation.md)

## Notes

- V: the whole function was read, and the comparator and the sort routine were read at their heads to identify them.
- I: kind2 maps each Throw ability
  (ids 0x17E..0x189) to a thrown item type.

## Open questions

None recorded.
