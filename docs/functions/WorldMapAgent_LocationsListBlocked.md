# WorldMapAgent_LocationsListBlocked

- **Address:** `0x140157BE4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char WorldMapAgent_LocationsListBlocked(int64_t agent)`
- **Callers:** sub_14022F868, BattleCommand_BuildScreen
- **Callees:** WorldMapBaseList_RecordAt

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells the list tasks that a confirm on the Locations list must be ignored: the list cannot take input or has no record under the cursor.

## Behavior

- V: returns 0 when the agent has no Locations list addon (+80).
- V: returns 1 when the addon's input test (vtable slot 3, WorldMapBaseList_CanTakeInput) fails or WorldMapBaseList_RecordAt(addon, cursor +816) returns null; else 0.
- V (callers' call sites): the generic list tasks call it for menu descriptor 154 before a confirm (sub_14022F868 at 0x140230B78, BattleCommand_BuildScreen at 0x1402E7225).

## State touched

- Calls: [WorldMapBaseList_RecordAt](WorldMapBaseList_RecordAt.md)

## Referenced by

- Observed behaviours: [LocationsListTabIndex](../behaviors/LocationsListTabIndex.md)

## Open questions

None recorded.
