# WorldMapRoutesAndLocationsFollowProgress

- **Kind:** observed behaviour
- **Scope:** engine (world map)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [WorldMapRoute_Refresh](../functions/WorldMapRoute_Refresh.md), [WorldMapRoute_SetGrey](../functions/WorldMapRoute_SetGrey.md), [WorldMapRoute_StartGrow](../functions/WorldMapRoute_StartGrow.md), [WorldMapRouteGrow_OnState](../functions/WorldMapRouteGrow_OnState.md), [WorldMapScreen_ScrollToProgress](../functions/WorldMapScreen_ScrollToProgress.md), [WorldMapBaseScreen_Open](../functions/WorldMapBaseScreen_Open.md), [WorldMapScreen_BindNodes](../functions/WorldMapScreen_BindNodes.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Routes are shown, hidden and greyed by the story progress row; a route grows between its two end points, forward or reversed; locations go into three lists by locations_list and are positioned by map_x / map_y.

## Behavior

- V: a route is greyed ('R_<name>_Color_Grayout') while the progress row's user_situation is 0 or met and the route is in the row's routes list; otherwise 'R_<name>_Color_Default'.
- V: the route's effect file is 'wm_route_<name>.uib' (UIAddon 138); it plays 'Show' / 'Hide' with state_suffix when forward, state_suffix_2 when reversed; UI sound 44 or 45.
- V: a route that is opened grows from town to town_2, or reversed when the current progress row has reverse_route set.
- V: a location with base set has the node 'Base<node_name>' and the screen file 'wm_base_<base_number>.uib' (UIAddon 137), otherwise 'Point<node_name>' and UIAddon 141; its picture is the Icon row 21 pattern filled with picture.
- V: locations_list 1 suppresses the info panel; values above 2 go to a separate list.
- V: the progress row's map_x / map_y (both not -1) are the scroll target.
- V: the town menu gets item 47200 (Poachers' Den) when event variable 144 is non-zero and the settlement's poachers_den byte is set.

## Open questions

? what Town byte +0x33 and shorts +0x2E do (no reader found).
