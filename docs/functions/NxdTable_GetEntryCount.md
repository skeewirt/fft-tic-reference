# NxdTable_GetEntryCount

- **Address:** `0x1403D3A34`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `__int64 NxdTable_GetEntryCount(NxdTable *table, unsigned int key)`
- **Callers:** UITable_GetRowCount, UITable_GetRowByIndex, CharClut_ApplyToPalette, sub_1400C795C and about twenty more
- **Callees:** NxdSets_Find2, NxdSets_Find3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For a double / triple keyed table: the record count of the set key1 (double: its rows; triple: its children), or 0.

## Behavior

- V: mode = *(qword *)(table+56) - 1; mode 0 (value 1) or value 0 returns 0. set table = *(qword *)(*(qword *)(table+48) + 56) + 32 (the loaded buffer's index header). Mode 1 (double keyed) uses NxdSets_Find2 (12-byte sets), other modes NxdSets_Find3 (20-byte sets).
- V: found set: returns the int at set+8 (its count); not found: 0.

## State touched

- Calls: [NxdSets_Find2](NxdSets_Find2.md), [NxdSets_Find3](NxdSets_Find3.md)

## Referenced by

- Appears in flows: [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md)
- Called by: [MapAnim_ReadRows](MapAnim_ReadRows.md), [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md), [SettlementEvent_EvaluateConditions](SettlementEvent_EvaluateConditions.md), [Unit_GetVoicePatternId](Unit_GetVoicePatternId.md), [UserSituation_IsMet](UserSituation_IsMet.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Notes

The name is ours (IDB: sub_1403D3A34). The index layouts are the format NxdMultiKeyIndex (V against all 58 multi-key retail files).

## Open questions

None recorded.
