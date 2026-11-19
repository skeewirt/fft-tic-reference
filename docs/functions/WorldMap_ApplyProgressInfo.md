# WorldMap_ApplyProgressInfo

- **Address:** `0x140341094`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void WorldMap_ApplyProgressInfo(void)`
- **Callers:** WorldMap_InitLocations, sub_1402B340C, sub_1402D50E4
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryByKeys2, NxdEntry_GetRow, UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the world-map progress rows that the story counters select to the world-map location values.

## Behavior

- V: skipped while the low dword of g_EventSkipFlags is set.
- V: for each GameProgress (nxd 92) counter index i: counter = g_UserSituation +24 + 4i; row = GameProgress (i, counter); then the WorldMapProgressInfo (nxd 123) row named by the GameProgress columns world_map_progress_info (+0x08) and world_map_progress_info_2 (+0x0C).
- V: when that row's +0x1C (column user_situation) is 0 or UserSituation_IsMet holds, its +8 and +0xC (47 = none) are taken as location values (index 0 keeps +0xC as well).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UserSituation_IsMet](UserSituation_IsMet.md)

## Open questions

? where the location values are stored for the map screens (I: the progress row's keys are kept at world-map screen +3308 / +3312 by WorldMapScreen_SetProgress and compared with location ids by sub_14036E5DC, which marks the location records with state 3 / 2).
