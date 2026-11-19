# NxdTable_GetEntryByKeyIndex

- **Address:** `0x1403D3C98`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntry *NxdTable_GetEntryByKeyIndex(NxdTable *table, unsigned int key1, int index)`
- **Callers:** NxdTable_GetRowById (mode 2, index 0), UITable_GetRowByIndex, CharClut_ApplyToPalette, CharaAnim_ReadStep, UIAddonFFTOLauncher_ShowPage and five more
- **Callees:** NxdSets_Find2, NxdSets_Find3, NxdTable_GetEntryByKeys2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The index-th row of the set key1 (double keyed), or the first leaf of the index-th child of the set (triple keyed), reached through the file's set index and then the bound entries.

## Behavior

- V: mode 2: set = NxdSets_Find2(file +32, key1); index must be below the set's count (+8); the array record at set + int(set +4) + 12 * index gives (key1, key2); returns NxdTable_GetEntryByKeys2(table, key1, key2).
- V: other modes: set = NxdSets_Find3; index below the child count; walks from that child to its first descendant while a record's +8 count is positive (retail children have 0), needs a leaf count (+16) above 0, and returns NxdTable_GetEntryByKeys2(table, leaf key1, leaf key2) (that is the first leaf of child (key1, key2)).
- V: returns null when a set, index or leaf is missing.

## State touched

- Calls: [NxdSets_Find2](NxdSets_Find2.md), [NxdSets_Find3](NxdSets_Find3.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md)
- Reads: [NxdTable.handle](../structs/NxdTable.md#handle), [NexResourceHandle.data](../structs/NexResourceHandle.md#data), [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Referenced by

- Appears in flows: [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md)
- Called by: [ClassicSubtitles_Step](ClassicSubtitles_Step.md), [MapAnim_ReadRows](MapAnim_ReadRows.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [UserSituation_IsMet](UserSituation_IsMet.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Notes

So NxdTable_GetRowById(table, id) of a double-keyed table returns the FIRST row of set id (of a triple-keyed one: the first leaf of child (id, 0), through NxdTable_GetEntryByKeysIndex3). The array record's own row offset (+8) is not read here: the row comes from the bound entries.

## Open questions

None recorded.
