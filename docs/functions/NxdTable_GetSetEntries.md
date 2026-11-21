# NxdTable_GetSetEntries

- **Address:** `0x1403D3DEC`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntrySpan *NxdTable_GetSetEntries(NxdTable *table, NxdEntrySpan *out, unsigned int key1)`
- **Callers:** 22 readers (sub_1400C9DCC, sub_1400CB870, sub_1401004B4, sub_14015E0FC, sub_14016BC30 and others)
- **Callees:** NxdSets_Find2, NxdTable_GetEntryByKeys2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The rows of one set of a double-keyed table as a span of bound entries: (entry of the set's first record, record count).

## Behavior

- V: only mode 2; set = NxdSets_Find2(file +32, key1); out = (NxdTable_GetEntryByKeys2(table, first record's key1, key2), set count); else (null, 0).
- V: its callers walk the span as consecutive 16-byte entries (for example sub_14015E0FC steps entry + 16 * i), so the rows of one set must be consecutive in the bound entries: the file's arrays, concatenated in set order, must equal its flat entry table.

## State touched

- Calls: [NxdSets_Find2](NxdSets_Find2.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md)
- Reads: [NxdTable.handle](../structs/NxdTable.md#handle), [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Referenced by

- Appears in flows: [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md)
- Called by: [CharaRender_LoadMapLights](CharaRender_LoadMapLights.md), [MapMesh_ApplyPolygonRows](MapMesh_ApplyPolygonRows.md), [ZodiacStone_AnyMet](ZodiacStone_AnyMet.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Notes

The X6 row overlay rebuilds the index so this stays true after new keys (its tests walk every set of the result).

## Open questions

None recorded.
