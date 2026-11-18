# MapTextures_NameOfFrame

- **Address:** `0x1400CAA54`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `const char *MapTextures_NameOfFrame(void *textureSet, int slot, int frame, int source)`
- **Callers:** MapTextures_LoadMapSlots
- **Callees:** NxdTable_GetEntryByKeys3, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the file name of one frame of one slot of the map's textures; null when there is none.

## Behavior

- V: slot must be below 21; frame 0 and 1 are the colour and lighting names (type 0 and 1), frame 2 type 2, frames 3..101 further colour frames, 102 up further lighting frames; a source other than 0 gives null.
- V: the table row (map id, slot, type) is read; the name comes from the primary array at the variation index or, when a kind code is set, from the second array at the kind index; a frame above 0 replaces the name's trailing 0 with the frame number; the name must end in .tga after the copy.

## State touched

- Calls: [NxdTable_GetEntryByKeys3](NxdTable_GetEntryByKeys3.md), [Str_Format](Str_Format.md)

## Referenced by

- Called by: [MapTextures_LoadMapSlots](MapTextures_LoadMapSlots.md)
- Observed behaviours: [MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven](../behaviors/MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven.md), [MapTextureRowsPairEveryNameWithAFrameCount](../behaviors/MapTextureRowsPairEveryNameWithAFrameCount.md), [RandomBattleModeSelectsTheLightingVariantOfAMapsTextures](../behaviors/RandomBattleModeSelectsTheLightingVariantOfAMapsTextures.md)

## Open questions

None recorded.
