# NxdTable_GetEntryByKeys2

- **Address:** `0x1403D3B5C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntry *NxdTable_GetEntryByKeys2(NxdTable *table, unsigned int key1, unsigned int key2)`
- **Callers:** NxdTable_GetEntryByIndex, NxdTable_GetEntryByKeyIndex, NxdTable_GetSetEntries, OverrideEntry_LoadBattleEntries, EventNode_SetFromTable224 and about 25 more readers
- **Callees:** NxdEntries_Search2, NxdTable_GetEntryByKeysIndex3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The row entry of (key1, key2): for a double-keyed table the binary search over the bound entries; for a triple-keyed table the first leaf of child (key1, key2).

## Behavior

- V: mode (table +0x38) 0 or 1 returns null.
- V: mode 2: NxdEntries_Search2(entries +0x10, 0, count +0x28, key1 | key2 << 32): the 16-byte entries bound from the file's flat entry table, sorted by (key1, key2).
- V: other modes: NxdTable_GetEntryByKeysIndex3(table, key1, key2, 0).

## State touched

- Calls: [NxdEntries_Search2](NxdEntries_Search2.md), [NxdTable_GetEntryByKeysIndex3](NxdTable_GetEntryByKeysIndex3.md)
- Reads: [NxdTable.entries](../structs/NxdTable.md#entries), [NxdTable.count](../structs/NxdTable.md#count), [NxdTable.mode](../structs/NxdTable.md#mode)

## Referenced by

- Appears in flows: [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md)
- Called by: [CharClut_GetColorSkin](CharClut_GetColorSkin.md), [Deployment_LoadAreaPlacement](Deployment_LoadAreaPlacement.md), [Launcher_DrawPage](Launcher_DrawPage.md), [LoreDictionary_GetEntry](LoreDictionary_GetEntry.md), [NxdTable_GetEntryByIndex](NxdTable_GetEntryByIndex.md), [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetSetEntries](NxdTable_GetSetEntries.md), [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [Unit_GetVoicePatternId](Unit_GetVoicePatternId.md), [WorldMap_ApplyProgressInfo](WorldMap_ApplyProgressInfo.md), [ZodiacStone_FillDetail](ZodiacStone_FillDetail.md), [sub_14036E5DC](sub_14036E5DC.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Notes

UITable_GetRowByKeys wraps it with the registry lookup by table id. A key pair that is not a row returns null.

## Open questions

None recorded.
