# sub_1401CAFE0

- **Address:** `0x1401CAFE0`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `char sub_1401CAFE0(List *list)`
- **Callers:** sub_1401B011C
- **Callees:** UITable_GetRowByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The same sort name order for the 48-byte entries of the poacher list (PoachListEntry).

## Behavior

- V: insertion sort of 48-byte entries; the key is the poach id at entry +24, looked up in UI table 0xEC; the strings at row +0x14 (sort_name) are compared, ties fall back to the id.
- I: its list is the one PoachList_Build fills (48-byte entries with the poach id at +24).

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Observed behaviours: [PoachListSortOrders](../behaviors/PoachListSortOrders.md)

## Notes

Name is ours. The +0x14 string is reached as dword index 5 of the row, so the constant 0x14 does not appear in the body.

## Open questions

None recorded.
