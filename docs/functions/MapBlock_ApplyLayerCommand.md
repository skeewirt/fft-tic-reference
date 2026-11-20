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
- V: reads scene variables 39 (the story event number), 48 (map state), 36 (night) and 35 (weather level) and calls MapRow_SelectVariation with the map id on every call (any layer); the chosen index and kind code are stored in the global work record at +116 and +120 (MapBlock_RunCommand reads the index from there).
- V: for layer 0 with the graphics-mode flag non-zero: MapRenderer_ApplyMapRow, a second read of the Map row's chosen variation element, then MapMesh_Load (given scene variables 48 and 34, the index and the kind) when the mesh set's loaded-id field is -1, else MapRenderer_ReuseLoadedMesh.
- V: from the chosen element, its floats at +0x30 and +0x34 are stored into the battle control block at +689068 and +689072, and (value * 12 - 36) * 4096 as integers at +689084 and +689088.
- ?: no code reading those four battle control fields was found (the constructor clears them; BattleControl_FrameUpdate works near +689100 only).
- V: a mesh load that returns 0 is followed by MapTextures_Reset, the id fields of the texture set, MapTextures_LoadSystemSlots, MapTextures_LoadMapSlots and MapAnim_Load; any other result skips all of them (the result is tested right after the call).
- V: ids 15 and 33 skip the texture steps as well; id 53 sets one extra node bit; ids 6, 62 and 92 adjust single stock tile records.

## State touched

- Calls: [MapRow_SelectVariation](MapRow_SelectVariation.md), [MapRenderer_ApplyMapRow](MapRenderer_ApplyMapRow.md), [MapMesh_Load](MapMesh_Load.md), [MapRenderer_ReuseLoadedMesh](MapRenderer_ReuseLoadedMesh.md), [MapTextures_Reset](MapTextures_Reset.md), [MapTextures_LoadSystemSlots](MapTextures_LoadSystemSlots.md), [MapTextures_LoadMapSlots](MapTextures_LoadMapSlots.md), [MapAnim_Load](MapAnim_Load.md)
- Writes: [g_SceneTaskSlots](../globals/g_SceneTaskSlots.md)

## Referenced by

- Called by: [MapBlock_RunCommand](MapBlock_RunCommand.md)
- Observed behaviours: [AFailedMeshLoadSkipsEveryLaterRendererStep](../behaviors/AFailedMeshLoadSkipsEveryLaterRendererStep.md), [MapVariationChosenBySceneVariables](../behaviors/MapVariationChosenBySceneVariables.md)

## Open questions

?: the meaning of the block's record fields beyond the ones copied; who reads the four battle control fields written from the element's +0x30 and +0x34.
