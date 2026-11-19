# Item_CompareSortOrder

- **Address:** `0x14030E774`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Item_CompareSortOrder(const uint8_t *a, const uint8_t *b)`
- **Callers:** Unit_ListThrowableItems, sub_14030EEF0 (as a qsort comparator)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

qsort comparator of two item-id bytes: -1 / 0 / 1 from the Item row dword +0x28 (column sort_order), smaller first.

## Behavior

- V: looks up the Item row of each id and compares the dword at row +0x28.
- V: used by Unit_ListThrowableItems and sub_14030EEF0.

## Open questions

None recorded.
