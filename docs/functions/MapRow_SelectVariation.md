# MapRow_SelectVariation

- **Address:** `0x140254B8C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapRow_SelectVariation(int *variation, int *kind, int mapId, int sceneVar35, int sceneVar36, int sceneVar48, int sceneVar39)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** NxdTable_GetRowById, UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses which variation struct of a map's Map row applies now, and a kind code, from four scene variables.

## Behavior

- V: both outputs start at 0; no Map row, or a map id of 0 or less, returns with them at 0.
- V: the variation structs (72 bytes) are tried from the last to the first (index 0 is the fallback); a struct matches when its selector fields equal the scene values or hold the wildcard (2, 5, -1), its fixed field is 0 and, when it names a condition row, the condition accepts the scene value; one more field may name a user situation that must hold.
- V: the kind code (1..6) comes from the matched struct's type field in the other branch of the function.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md), [UserSituation_IsMet](UserSituation_IsMet.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md), [RandomBattleModeSelectsTheLightingVariantOfAMapsTextures](../behaviors/RandomBattleModeSelectsTheLightingVariantOfAMapsTextures.md)

## Open questions

?: what each scene variable means; the second branch selected by the global at 0x141853C08.
