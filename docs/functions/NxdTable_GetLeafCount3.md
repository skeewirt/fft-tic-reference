# NxdTable_GetLeafCount3

- **Address:** `0x1403D3A84`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `int NxdTable_GetLeafCount3(NxdTable *table, unsigned int key1, unsigned int key2)`
- **Callers:** sub_1402FB7C8, sub_140343AF8
- **Callees:** NxdSets_Find3, NxdSet3_FindChild

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The number of leaves (key3 rows) of child (key1, key2) of a triple-keyed table, or 0.

## Behavior

- V: mode below 3 returns 0; NxdSets_Find3 then NxdSet3_FindChild; returns the child's +16 count.

## State touched

- Calls: [NxdSets_Find3](NxdSets_Find3.md), [NxdSet3_FindChild](NxdSet3_FindChild.md)
- Reads: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Referenced by

- Called by: [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md)

## Open questions

None recorded.
