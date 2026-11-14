# NxdSets_Find2

- **Address:** `0x1403D3878`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdSet2 *NxdSets_Find2(NxdSetTable *sets, unsigned int key1)`
- **Callers:** NxdTable_GetEntryCount, NxdTable_GetEntryByKeyIndex, NxdTable_GetSetEntries, and five readers that scan a set's array themselves (sub_1400DA5D8, sub_1400DAD58, sub_1400DB384, sub_1400F94DC, sub_14015E0FC)
- **Callees:** NxdSets_Search2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the set of a key1 in a double-keyed file: binary search over the 12-byte set records the index header at file +32 points to.

## Behavior

- V: sets = (int offset relative to itself, int count); record i at sets + offset + 12 * i; key1 at record +0, compared unsigned.
- V: tests the middle record first, then continues in NxdSets_Search2 on the half that can hold the key; returns the record or null (count 0 or not found).

## State touched

- Calls: [NxdSets_Search2](NxdSets_Search2.md)
- Reads: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Referenced by

- Called by: [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetSetEntries](NxdTable_GetSetEntries.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Notes

The callers pass *(table +0x30 handle)->data + 32, so they read the loaded buffer, not the table object.

## Open questions

None recorded.
