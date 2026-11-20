# MapRow_SelectVariation

- **Address:** `0x140254B8C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapRow_SelectVariation(int *variation, int *kind, int mapId, int sceneVar35, int sceneVar36, int sceneVar48, int sceneVar39)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** NxdTable_GetRowById, UserSituation_IsMet, NxdRegistry_Find, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses which variation struct of a map's Map row applies now, and a kind code, from four scene variables.

## Behavior

- V: both outputs start at 0; no Map row, or a map id of 0 or less, returns with them at 0.
- V: the variation structs (72 bytes) are tried from the last to the first (index 0 is the fallback); a struct matches when its selector fields equal the scene values or hold the wildcard (2, 5, -1), its fixed field is 0 and, when it names a condition row, the condition accepts the scene value; one more field may name a user situation that must hold.
- V: the arguments after the map id are the weather level (scene variable 35), the night flag (variable 36), the map state (variable 48) and the story event number (variable 39), as MapBlock_ApplyLayerCommand reads them.
- V: story branch (g_BattleModeFlag is not 1): the elements are tried from the count minus 1 down to 1; element 0 is never tested and is the result when none matches (index 0, kind 0). An element is accepted when +0x10 is 0, +0 is 2 or the night flag, +4 is 5 or the weather level, +8 is -1 or the map state, and either +0xC is 0 or the MapVariationEvent row of that key exists and its event (+8) or one of its more_events equals the event number (a missing row rejects the element), and either +0x24 is 0 or UserSituation_IsMet accepts it.
- V: random-battle branch (g_BattleModeFlag is 1): the kind wanted is 1 / 2 / 3 by day and 4 / 5 / 6 at night (night flag non-zero), for weather level 0 or 5 and above / 1..2 / 3..4; the last element (count minus 1 down to 1) whose +0x10 equals the wanted kind is chosen (index 0 when none), and the wanted kind is returned as the kind code either way. None of the other selectors is tested in this branch.
- V: the table MapVariationEvent is fetched here and nowhere else; MapVariationRandomBattle is never fetched.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md), [UserSituation_IsMet](UserSituation_IsMet.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)
- Reads: [g_BattleModeFlag](../globals/g_BattleModeFlag.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md), [MapTablesBytesAndTablesNothingReads](../behaviors/MapTablesBytesAndTablesNothingReads.md), [MapVariationChosenBySceneVariables](../behaviors/MapVariationChosenBySceneVariables.md), [RandomBattleModeSelectsTheLightingVariantOfAMapsTextures](../behaviors/RandomBattleModeSelectsTheLightingVariantOfAMapsTextures.md), [ScenarioMapStateIsOnlyAMapVariationSelector](../behaviors/ScenarioMapStateIsOnlyAMapVariationSelector.md), [ScenarioWeatherLevelAndNightFlag](../behaviors/ScenarioWeatherLevelAndNightFlag.md)

## Open questions

?: what the loaders do with the kind code (which texture and lighting set they pick).
