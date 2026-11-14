# NxdSets_Find3

- **Address:** `0x1403D38DC`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdSet3 *NxdSets_Find3(NxdSetTable *sets, unsigned int key1)`
- **Callers:** NxdTable_GetEntryCount, NxdTable_GetEntryByKeyIndex, NxdTable_GetEntryByKeysIndex3, NxdTable_GetLeafCount3, sub_1400D5934 and the five set-scanning readers
- **Callees:** NxdSets_Search3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the set of a key1 in a triple-keyed file: the same search over 20-byte set records.

## Behavior

- V: as NxdSets_Find2 with a 20-byte stride; the continuation is NxdSets_Search3.
- V: NxdTable_GetEntryCount also uses it for any table mode other than 1 and 2.

## State touched

- Calls: [NxdSets_Search3](NxdSets_Search3.md)
- Reads: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Referenced by

- Called by: [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetEntryByKeysIndex3](NxdTable_GetEntryByKeysIndex3.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetLeafCount3](NxdTable_GetLeafCount3.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Open questions

None recorded.
