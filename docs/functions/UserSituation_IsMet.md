# UserSituation_IsMet

- **Address:** `0x1400FF8A4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool UserSituation_IsMet(void *unused, unsigned int situation)`
- **Callers:** BarTop_Setup and about 50 more (JobTree_FillJobRecords, Shop_GetUiRowId, sub_1401607D4, sub_140341094, ...)
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryCount, NxdTable_GetEntryByKeyIndex, NxdEntry_GetRow, UserSituation_TestCheck

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether a UserSituation condition (nxd table 90, keyed by situation and entry) holds; the UI asks it to show or lock features.

## Behavior

- V: 0 holds always; otherwise for each entry of the key (NxdTable_GetEntryCount / GetEntryByKeyIndex) it runs the checks of the row (type at +8 + 4k, the union id at +24 + 8k, values at +44 + 4k and +80 + 4k, the IsTrueForSuccess byte at +92 + k) through UserSituation_TestCheck.
- V: a check whose result differs from its IsTrueForSuccess byte moves on to the next entry; reaching a check type 0 first returns false. After the last entry it returns true.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UserSituation_TestCheck](UserSituation_TestCheck.md)

## Referenced by

- Called by: [BarTop_Setup](BarTop_Setup.md), [MapRow_SelectVariation](MapRow_SelectVariation.md), [TavernRumour_IsAvailable](TavernRumour_IsAvailable.md)
- Observed behaviours: [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md)

## Notes

Name is ours (was sub_1400FF8A4). Situation 3220 (one entry: type 6 on id 0, value 450, IsTrueForSuccess 0) opens the tavern errand row.

## Open questions

? the meaning of the union type 121 in the row (the id is read alone).
