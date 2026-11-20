# MapVariationChosenBySceneVariables

- **Kind:** observed behaviour
- **Scope:** engine (Map row variation elements, scene variables 35, 36, 39 and 48)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md), [MapBlock_ApplyLayerCommand](../functions/MapBlock_ApplyLayerCommand.md), [MapRenderer_ApplyMapRow](../functions/MapRenderer_ApplyMapRow.md), [MapRenderer_ApplyVariationEffects](../functions/MapRenderer_ApplyVariationEffects.md), [MapVariationStruct](../structs/MapVariationStruct.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which variation element of a map's Map row is drawn is decided once per map load from four scene variables in a story battle, and from the weather and night alone in a random battle. The element then sets the map's post-effect rows, its effect scale and its two background colours.

## Behavior

- V: MapBlock_ApplyLayerCommand reads scene variable 39 (the story event number), 48 (the map state), 36 (the night flag) and 35 (the weather level) and passes them with the map id to MapRow_SelectVariation; the chosen index and the kind code go to the global work record at +116 and +120.
- V: story branch (g_BattleModeFlag not 1): elements count - 1 down to 1 are tried in that order; element 0 is never tested and is the fallback. An element needs lighting_kind 0, night 2 or equal, weather 5 or equal, map_state -1 or equal, map_variation_event 0 or a MapVariationEvent row whose event or more_events holds the event number, and user_situation 0 or a met UserSituation.
- V: random branch (g_BattleModeFlag 1): only the weather level and the night flag are used. Wanted kind: weather 0 or 5 and above 1 (day) / 4 (night); weather 1..2 2 / 5; weather 3..4 3 / 6. The last element from count - 1 down to 1 with that lighting_kind is chosen, element 0 when none; the kind code is returned either way (it is 0 in the story branch).
- V: MapRenderer_ApplyMapRow applies the chosen element: the four post-effect keys (glare, colour lookup, depth lookup, depth of field) through MapRenderer_ApplyVariationEffects, the depth bias key, the effect scale, lut_row_offset and the bytes +0x45 and +0x47.
- V: MapMesh_Load receives the chosen index and the kind code; the texture-name builder reads the second name array of its texture row at the kind code minus 1 (see the behavior of the random-battle texture names).
- M: stock rows: 91 Map rows have one element, 18 have seven (the random-battle maps 71..90), the others two to four, one nine; night is 2 on 258 of 271 elements, weather 5 on 259, map_state -1 on 269; lighting_kind is 0 on 157 elements and 1..6 on 19 each; the nonzero user_situation keys are 4001 and 4002 (one element each).
- M: MapVariationEvent has 14 rows; only one has more_events (ten entries).

## Open questions

? what the loaders do with the kind code beyond the texture-name builder; the random branch treats weather 5 and above like 0 (read from the compare chain, not seen in play).
