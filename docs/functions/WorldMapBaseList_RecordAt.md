# WorldMapBaseList_RecordAt

- **Address:** `0x140160790`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t WorldMapBaseList_RecordAt(int64_t self, int index)`
- **Callers:** WorldMapAgent_LocationsListBlocked, WorldMapBaseList_OnEvent, LegacyMenu_PickLocation, sub_14036E5DC
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the 64-byte location record at an index of the current tab of the Locations list addon (struct WorldMapBaseList), or null.

## Behavior

- V: null when the tab +1840 is above 2 (unsigned), the index is negative or not below the tab's record count; else begin + 64 * index of vector +1704 + 32 * tab.

## Referenced by

- Called by: [WorldMapAgent_LocationsListBlocked](WorldMapAgent_LocationsListBlocked.md), [WorldMapBaseList_OnEvent](WorldMapBaseList_OnEvent.md)
- Observed behaviours: [LocationsListTabIndex](../behaviors/LocationsListTabIndex.md)

## Open questions

None recorded.
