# NxdTable_GetEntryByKeysIndex3

- **Address:** `0x1403D3D58`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntry *NxdTable_GetEntryByKeysIndex3(NxdTable *table, unsigned int key1, unsigned int key2, int index)`
- **Callers:** NxdTable_GetRowById (mode 3, keys (id, 0), index 0), NxdTable_GetEntryByKeys2 (mode 3, index 0), sub_1400CA47C
- **Callees:** NxdSets_Find3, NxdSet3_FindChild, NxdTable_GetEntryByKeys3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The index-th leaf of child (key1, key2) of a triple-keyed table, through the set index and then the bound entries.

## Behavior

- V: mode below 3 returns null; set = NxdSets_Find3(file +32, key1); child = NxdSet3_FindChild(set, key2); the leaf at child + int(child +12) + 20 * index gives (key1, key2, key3); returns NxdTable_GetEntryByKeys3.
- V: the index is not checked against the leaf count (+16) here.

## State touched

- Calls: [NxdSets_Find3](NxdSets_Find3.md), [NxdSet3_FindChild](NxdSet3_FindChild.md), [NxdTable_GetEntryByKeys3](NxdTable_GetEntryByKeys3.md)
- Reads: [NxdTable.handle](../structs/NxdTable.md#handle), [NexResourceHandle.data](../structs/NexResourceHandle.md#data), [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Referenced by

- Called by: [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Open questions

? whether every caller keeps the index below the leaf count.
