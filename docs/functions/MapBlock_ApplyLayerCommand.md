# MapBlock_ApplyLayerCommand

- **Address:** `0x1402523B0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapBlock_ApplyLayerCommand(void *block, void *tables, int layer)`
- **Callers:** MapBlock_RunCommand
- **Callees:** MapRow_SelectVariation, MapRenderer_ApplyMapRow, MapMesh_Load, MapRenderer_ReuseLoadedMesh, MapTextures_Reset, MapTextures_LoadSystemSlots, MapTextures_LoadMapSlots, MapAnim_Load

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies one layer's records of the loaded map block to the draw tables and, for layer 0 in the enhanced graphics mode, starts the map mesh, texture and anim loads.

## Behavior

- V: reads the map block's u16 token stream and fills one 0xA8-byte layer record; writes 0x79 to the word after the battle tile table.
- V: copies the layer's tile and polygon records from the block into the global draw tables; this part does not read any renderer data table.
- V: for layer 0 with the graphics-mode flag non-zero: MapRow_SelectVariation, MapRenderer_ApplyMapRow, a second read of the Map row for two placement floats, then MapMesh_Load when the mesh set's loaded-id field is -1, else MapRenderer_ReuseLoadedMesh.
- V: a mesh load that returns 0 is followed by MapTextures_Reset, the id fields of the texture set, MapTextures_LoadSystemSlots, MapTextures_LoadMapSlots and MapAnim_Load; any other result skips all of them (the result is tested right after the call).
- V: ids 15 and 33 skip the texture steps as well; id 53 sets one extra node bit; ids 6, 62 and 92 adjust single stock tile records.

## State touched

- Calls: [MapRow_SelectVariation](MapRow_SelectVariation.md), [MapRenderer_ApplyMapRow](MapRenderer_ApplyMapRow.md), [MapMesh_Load](MapMesh_Load.md), [MapRenderer_ReuseLoadedMesh](MapRenderer_ReuseLoadedMesh.md), [MapTextures_Reset](MapTextures_Reset.md), [MapTextures_LoadSystemSlots](MapTextures_LoadSystemSlots.md), [MapTextures_LoadMapSlots](MapTextures_LoadMapSlots.md), [MapAnim_Load](MapAnim_Load.md)
- Writes: [g_SceneTaskSlots](../globals/g_SceneTaskSlots.md)

## Referenced by

- Called by: [MapBlock_RunCommand](MapBlock_RunCommand.md)
- Observed behaviours: [AFailedMeshLoadSkipsEveryLaterRendererStep](../behaviors/AFailedMeshLoadSkipsEveryLaterRendererStep.md)

## Open questions

?: the meaning of the block's record fields beyond the ones copied.
