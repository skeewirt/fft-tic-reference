# NxdTable_GetEntryByIndex

- **Address:** `0x1403D3BE4`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntry *NxdTable_GetEntryByIndex(NxdTable *table, unsigned int64 index)`
- **Callers:** NxdTable_GetRowById (the contiguous-keys path), UITable_GetRow and about 45 other readers
- **Callees:** NxdTable_GetEntryByKeys2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the entry at a row position; null when the position is not below the row count.

## Behavior

- V: mode 1: null when index >= count (+40), else entries (+16) + 16 * index.
- V: mode 2: the index-th SET of the buffer's set table (index below the set count, file +36); a set with a positive count gives its first array record's keys; returns NxdTable_GetEntryByKeys2 of them (the set's first row).
- V: other modes: the index-th triple set, descends to the first child while a record's +8 count is positive, needs a leaf count above 0, and returns NxdTable_GetEntryByKeys2 of the first leaf's (key1, key2) (that child's first leaf).

## State touched

- Calls: [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md)

## Referenced by

- Called by: [NxdTable_GetRowById](NxdTable_GetRowById.md), [StatusLists_BuildOrder](StatusLists_BuildOrder.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Notes

Item-en with key 300 after 0..260 and the flag kept: key 300 asked position 300 of 262 rows (live read).

## Open questions

None recorded.
