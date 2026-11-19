# WorldMapRoute_SetGrey

- **Address:** `0x14015DFCC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapRoute_SetGrey(void *screen, int route, int grey)`
- **Callers:** not recorded
- **Callees:** GUINode_PlayState, GUINode_StopState, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays a route's grey or default colour state.

## Behavior

- V: plays 'R_%s_Color_Grayout' when grey is non-zero, else 'R_%s_Color_Default' (and stops the other) on the route node at screen +512.

## State touched

- Calls: [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md), [Str_Format](Str_Format.md)

## Referenced by

- Called by: [WorldMapRoute_Refresh](WorldMapRoute_Refresh.md)
- Observed behaviours: [WorldMapRoutesAndLocationsFollowProgress](../behaviors/WorldMapRoutesAndLocationsFollowProgress.md)

## Open questions

None recorded.
