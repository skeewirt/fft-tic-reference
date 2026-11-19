# WorldMapRoute_StartGrow

- **Address:** `0x140157E88`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapRoute_StartGrow(void *screen, const void *request)`
- **Callers:** not recorded
- **Callees:** UITable_GetRowByKey, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the grow animation of a route between two locations.

## Behavior

- V: creates UIAddonFFTOWorldMapRouteGrowEffect from 'wm_route_<Route name (+4)>.uib' (UIAddon row 138).
- V: the direction byte +209 is flipped when the request's byte +24 is 0 and the current WorldMapProgressInfo row has reverse_route (+0x28) set.
- V: effect +188 / +192 = start / end location (Route town +8 / town_2 +0xC, swapped when flipped); +196 / +200 = Route +8 / +0xC.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [Str_Format](Str_Format.md)

## Referenced by

- Observed behaviours: [WorldMapRoutesAndLocationsFollowProgress](../behaviors/WorldMapRoutesAndLocationsFollowProgress.md)

## Open questions

None recorded.
