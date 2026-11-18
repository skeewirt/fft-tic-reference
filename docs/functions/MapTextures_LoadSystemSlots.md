# MapTextures_LoadSystemSlots

- **Address:** `0x1400CA47C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MapTextures_LoadSystemSlots(void *textureSet)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** sub_1403CAC84

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Requests the 8 system textures of the map: names from RefinedBgSystemTexture, default colour table when there is none.

## Behavior

- V: for slot 0..7 reads leaf n of the child (map id, 0) of table 141; the name comes from the array chosen by the kind code or the variation; the path is the map id in three digits as a folder plus the name and .tga.
- V: no row, an empty array or an empty first character uses the stock default colour table file; there is no bound on the map id here.

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md), [MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven](../behaviors/MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven.md), [RandomBattleModeSelectsTheLightingVariantOfAMapsTextures](../behaviors/RandomBattleModeSelectsTheLightingVariantOfAMapsTextures.md)

## Open questions

?: the texture manager's answer to a missing file.
