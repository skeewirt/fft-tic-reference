# MapTextures_LoadMapSlots

- **Address:** `0x1400CA690`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MapTextures_LoadMapSlots(void *textureSet)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** MapTextures_SlotVariantCode, MapTextures_NameOfFrame, sub_1403CAC84

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Requests the map's colour and lighting textures from the RefinedBgTexture rows, deduplicating equal names.

## Behavior

- V: the whole row read is conditional on the set's map id being 127 or less (unsigned compare of the id field with 0x7F) and the texture-source field being 0; otherwise the slot count is 0 and nothing is requested.
- V: slot count = children of the map's set; for each slot two variant codes (MapTextures_SlotVariantCode), then 201 frame indices; each name from MapTextures_NameOfFrame becomes a path of the map id in three digits and the name; a name seen earlier in the same frame column reuses its handle.

## State touched

- Calls: [MapTextures_SlotVariantCode](MapTextures_SlotVariantCode.md), [MapTextures_NameOfFrame](MapTextures_NameOfFrame.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md), [MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven](../behaviors/MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven.md), [MapTextureRowsPairEveryNameWithAFrameCount](../behaviors/MapTextureRowsPairEveryNameWithAFrameCount.md), [RandomBattleModeSelectsTheLightingVariantOfAMapsTextures](../behaviors/RandomBattleModeSelectsTheLightingVariantOfAMapsTextures.md)

## Open questions

None recorded.
