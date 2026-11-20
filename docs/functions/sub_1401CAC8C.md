# sub_1401CAC8C

- **Address:** `0x1401CAC8C`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `char sub_1401CAC8C(List *list)`
- **Callers:** sub_1401ABE14
- **Callees:** UITable_GetRowByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Insertion sort of 24-byte poach entries by the PoachItem sort byte (+0x35), larger value first; ties fall back to the id, smaller first.

## Behavior

- V: fetches the PoachItem row (UI table 0xEC) of each entry's first dword; when both rows exist and their bytes at +0x35 (column sort_order) differ, the entry with the larger byte moves before the other.
- V: otherwise the entry with the smaller id moves first.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [sub_1401ABE14](sub_1401ABE14.md)
- Observed behaviours: [PoachListSortOrders](../behaviors/PoachListSortOrders.md)

## Notes

Name is ours. The direction (larger byte first) is as the code reads; the column's name suggests an ascending key.

## Open questions

? which screen uses this order and which the name order.
