# PlaceName_GetText

- **Address:** `0x1400FB44C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `const char *PlaceName_GetText(unsigned key)`
- **Callers:** SaveLoadList_FillItem, sub_140102BDC, sub_140117684, sub_140144E24, sub_140148D24, sub_140148DE4, sub_14014F264, sub_140151464, sub_140158CB0, sub_140160410
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the text of a PlaceName row (table 85) by its key, or the empty string.

## Behavior

- V: uses the cached table pointer qword_143CDA318; when it is zero the table is fetched from the registry by id 85, and a missing registry or table returns the empty string.
- V: key 0 returns the empty string; a missing row returns it too.
- V: otherwise returns the string at row + 12 + (the dword at row + 12): the text offset stored at row +12 is counted from row +12.
- V: the Map row's three name members (place_name, place_name_2, place_name_3) are keys of this table; the title, the save list and the map-name nodes read them through this function.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [MapTitle_SetFromMapId](MapTitle_SetFromMapId.md), [WorldMapBaseList_DrawRow](WorldMapBaseList_DrawRow.md)
- Observed behaviours: [MapRowPlaceNameKeys](../behaviors/MapRowPlaceNameKeys.md)

## Notes

Keys that name no row (for example 10100 on five Map rows, M) give the empty text, not an error.

## Open questions

None recorded.
