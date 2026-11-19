# WorldMapRoute_Refresh

- **Address:** `0x14015B3AC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapRoute_Refresh(void *screen, const char *flag, int route)`
- **Callers:** sub_1401586BC, sub_14015BB64, WorldMap_InitLocations
- **Callees:** WorldMapRoute_SetGrey, UserSituation_IsMet, GUINode_PlayState, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows or hides one route on the world map and sets its grey state.

## Behavior

- V: for a route id a3 up to 50 (Route table 97, +4 = the route's node name): plays 'Show_R_%s' or 'Hide_R_%s' by *a2.
- V: then grey = (progress row user_situation (+0x1C) is 0 or met) and the route is in the progress row's routes list (+0x10); calls WorldMapRoute_SetGrey(screen, route, grey).

## State touched

- Calls: [WorldMapRoute_SetGrey](WorldMapRoute_SetGrey.md), [UserSituation_IsMet](UserSituation_IsMet.md), [GUINode_PlayState](GUINode_PlayState.md), [Str_Format](Str_Format.md)

## Referenced by

- Observed behaviours: [WorldMapRoutesAndLocationsFollowProgress](../behaviors/WorldMapRoutesAndLocationsFollowProgress.md)

## Open questions

None recorded.
