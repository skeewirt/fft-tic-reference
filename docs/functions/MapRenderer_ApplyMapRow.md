# MapRenderer_ApplyMapRow

- **Address:** `0x1400D5374`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapRenderer_ApplyMapRow(void *renderer, unsigned mapId, int variation, int kind)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** MapTextures_Reset, MapMesh_Reset, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tears down a mesh set that belongs to another map or variation, then applies the chosen variation of the map's Map row to the renderer's post-effect settings.

## Behavior

- V: when the mesh set holds an id and it differs from the requested one, or the kind code is non-zero, or the texture set was built for another variation: the mesh and texture sets are reset (MapTextures_Reset, MapMesh_Reset) and the loaded-id field set to -1.
- V: the Map row of the id is read with the generic row lookup; a missing row ends the function with nothing applied.
- V: the variation struct at index `variation` feeds sub_1400CF2A8 (post-effect lookup tables and light) and a few renderer constants.

## State touched

- Calls: [MapTextures_Reset](MapTextures_Reset.md), [MapMesh_Reset](MapMesh_Reset.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)

## Open questions

?: the constants' use.
