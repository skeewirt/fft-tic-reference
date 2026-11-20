# MapTitle_SetFromMapId

- **Address:** `0x140148D24`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char MapTitle_SetFromMapId(void *window, int mapId)`
- **Callers:** sub_1401EF0D8
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, PlaceName_GetText, MapTitleLabel_SetText

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the title text of a map into the window's map-title label from the map id's Map row.

## Behavior

- V: fetches the Map row (table 60, cache qword_143CD9FA0) of the id.
- V: takes the text of the PlaceName key in row +0x8 (place_name) through PlaceName_GetText and the row byte +0x1C (title_ja_state) and hands both to MapTitleLabel_SetText.
- V: the Map row's place_name_2 and place_name_3 are not read here (the save list reads them).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [PlaceName_GetText](PlaceName_GetText.md), [MapTitleLabel_SetText](MapTitleLabel_SetText.md)

## Referenced by

- Observed behaviours: [MapRowPlaceNameKeys](../behaviors/MapRowPlaceNameKeys.md)

## Open questions

? which screen's window it fills (only the caller sub_1401EF0D8 was noted).
