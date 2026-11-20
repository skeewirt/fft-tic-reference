# MapRenderer_ApplyMapRow

- **Address:** `0x1400D5374`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapRenderer_ApplyMapRow(void *renderer, unsigned mapId, int variation, int kind)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** MapTextures_Reset, MapMesh_Reset, NxdTable_GetRowById, MapRenderer_ApplyVariationEffects, EffectNxd_DepthBiasFloat

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tears down a mesh set that belongs to another map or variation, then applies the chosen variation of the map's Map row to the renderer's post-effect settings.

## Behavior

- V: when the mesh set holds an id and it differs from the requested one, or the kind code is non-zero, or the texture set was built for another variation: the mesh and texture sets are reset (MapTextures_Reset, MapMesh_Reset) and the loaded-id field set to -1.
- V: the Map row of the id is read with the generic row lookup; a missing row ends the function with nothing applied.
- V: the variation element at index `variation` (row + variations offset + 72 * index) feeds MapRenderer_ApplyVariationEffects with its post-effect keys at +0x14 (glare), +0x18 (LUT), +0x1C (depth LUT) and +0x28 (depth of field); those four offsets are read in the callee as dword indices 5, 6, 7 and 10, so they do not appear in this body.
- V: the element's byte +0x45 is stored as a dword into the mesh set at +6070656; byte +0x46 into the renderer sub-object at +1097 (lut_row_offset); +0x47 == 0 into the renderer byte +147905 (with +147904 set to 1).
- V: element +0x2C non-zero: EffectNxd_DepthBiasFloat (DepthBias row, key = the member) replaces the renderer's depth bias at +147840.
- V: element float +0x20 is stored in dword_1407DC6DC; the effect scale limits are max(1.0, dword_1407DC6E0, +0x20, dword_1407DC6E4) times dword_142E7FAF8, stored times 4096 in dword_1407DC4F8 and times 2048 in dword_1407DC6C8 (the same formula as EffectNxd_LoadRow).

## State touched

- Calls: [MapTextures_Reset](MapTextures_Reset.md), [MapMesh_Reset](MapMesh_Reset.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [MapRenderer_ApplyVariationEffects](MapRenderer_ApplyVariationEffects.md), [EffectNxd_DepthBiasFloat](EffectNxd_DepthBiasFloat.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)
- Observed behaviours: [MapTablesBytesAndTablesNothingReads](../behaviors/MapTablesBytesAndTablesNothingReads.md), [MapVariationChosenBySceneVariables](../behaviors/MapVariationChosenBySceneVariables.md)

## Open questions

?: what the two derived scale globals and the +0x45 / +0x47 flags drive in the drawn picture.
