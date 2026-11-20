# Unit_GetVoicePatternId

- **Address:** `0x1401EDD50`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Unit_GetVoicePatternId(int job, int nameKey, ...)`
- **Callers:** sub_1400F8930, sub_1400F8D6C, sub_1401D7874, sub_1401E37D4, sub_1401EDB88 and others
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, NxdTable_GetEntryCount, NxdTable_GetEntryByKeys2, UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the voice pattern id of a unit: from its job row, else by a rule over the CharaName rows.

## Behavior

- V: the Job row's voice_pattern column (+0x1C, Job table 46) when non-zero is returned as the unit's voice pattern id; otherwise a rule over CharaName rows (checked with UserSituation_IsMet).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md), [UserSituation_IsMet](UserSituation_IsMet.md)

## Notes

Name is ours; read as the source of the pattern id only.

## Open questions

? the exact CharaName rule.
