# NxdTable_GetEntryByKeys3

- **Address:** `0x1403D3BAC`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntry *NxdTable_GetEntryByKeys3(NxdTable *table, unsigned int key1, unsigned int key2, unsigned int key3)`
- **Callers:** NxdTable_GetEntryByKeysIndex3, sub_1400CAA54, sub_1400CACDC, sub_1400D5934, sub_1402FB7C8, sub_140343AF8
- **Callees:** NxdEntries_Search3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The row entry of (key1, key2, key3) in a triple-keyed table: the binary search over the bound entries.

## Behavior

- V: mode below 3 returns null; else NxdEntries_Search3(entries +0x10, 0, count +0x28, {key1, key2, key3}).

## State touched

- Calls: [NxdEntries_Search3](NxdEntries_Search3.md)
- Reads: [NxdTable.entries](../structs/NxdTable.md#entries), [NxdTable.count](../structs/NxdTable.md#count), [NxdTable.mode](../structs/NxdTable.md#mode)

## Referenced by

- Appears in flows: [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md)
- Called by: [MapMesh_FindNodeRows](MapMesh_FindNodeRows.md), [MapTextures_NameOfFrame](MapTextures_NameOfFrame.md), [MapTextures_SlotVariantCode](MapTextures_SlotVariantCode.md), [NxdTable_GetEntryByKeysIndex3](NxdTable_GetEntryByKeysIndex3.md), [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md), [SettlementEvent_EvaluateConditions](SettlementEvent_EvaluateConditions.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Open questions

None recorded.
