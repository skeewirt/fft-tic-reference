# MapMesh_Load

- **Address:** `0x1400C7F54`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MapMesh_Load(void *meshSet, unsigned mapId, int sceneVar48, int sceneVar34, int variation, int kind)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** MapMesh_StockNodeOffset, MapMesh_FindNodeRows, MapMesh_InitNodeFlags

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the map's mesh file into the mesh set and sets up its node rows; 0 = built, 1 = nothing built.

## Behavior

- V: ids 15 and 33 return 1 at once. The path is the map id in three digits inside the meshes folder (lower-cased); the open, the size and the read go through the resource manager and each failure returns 1 with no message.
- V: a size over 7,534,452 bytes returns 1; the 48-byte header must carry the format tag and, at +8, the requested map id, else the buffer is freed and 1 is returned (seen in the instructions and in the headers of three stock files); +12 is the layer count (1 in those files).
- V: per layer the tile-index, height and polygon arrays are copied in; for stock maps up to id 116 MapMesh_StockNodeOffset shifts node positions.
- V: stores the map id in the mesh set, reads the node rows with MapMesh_FindNodeRows (variation key when the kind code is 0, else 0; a second try with key 0), then MapMesh_InitNodeFlags and the node ordering; returns 0.

## State touched

- Calls: [MapMesh_StockNodeOffset](MapMesh_StockNodeOffset.md), [MapMesh_FindNodeRows](MapMesh_FindNodeRows.md), [MapMesh_InitNodeFlags](MapMesh_InitNodeFlags.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)
- Observed behaviours: [AFailedMeshLoadSkipsEveryLaterRendererStep](../behaviors/AFailedMeshLoadSkipsEveryLaterRendererStep.md), [MapMeshAndAnimFilesCarryTheirOwnMapId](../behaviors/MapMeshAndAnimFilesCarryTheirOwnMapId.md), [ScenarioMapStateIsOnlyAMapVariationSelector](../behaviors/ScenarioMapStateIsOnlyAMapVariationSelector.md)

## Open questions

?: what the texture manager does when a requested texture file is missing.
