# MapRendererBuildPath

- **Kind:** flow
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the Enhanced renderer builds the terrain of a battle map: from the map id to the requests for the mesh, the textures and the anim, and which data table rows steer each step. A mesh load that does not return success ends the build: every later step is skipped.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [Map_LoadBattleData](../functions/Map_LoadBattleData.md) | V | The map id arrives as a 16-bit argument and is stored in a 32-bit global when the map has a block. |
| <a id="2"></a>2 | [MapBlock_RunCommand](../functions/MapBlock_RunCommand.md) | V | The block's layer commands are run; the base layer's command calls the layer function with layer 0. |
| <a id="3"></a>3 | [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md) | V | Variation index and kind code chosen from the Map row's variation structs and four scene variables (0, 0 with no Map row). |
| <a id="4"></a>4 | [MapRenderer_ApplyMapRow](../functions/MapRenderer_ApplyMapRow.md) | V | A loaded mesh set of another map or variation is torn down; the variation's post-effect settings are applied (nothing when the Map row is missing). |
| <a id="5"></a>5 | [MapMesh_Load](../functions/MapMesh_Load.md) | V | The mesh file is opened, size-checked (7,534,452 bytes at most), its header tag and map id (+8) checked against the requested id, its layers copied, node rows read; 1 on any failure. |
| <a id="6"></a>6 | [MapTextures_LoadSystemSlots](../functions/MapTextures_LoadSystemSlots.md) | V | Only after a successful mesh load: eight system textures (RefinedBgSystemTexture, the stock default when no row). |
| <a id="7"></a>7 | [MapTextures_LoadMapSlots](../functions/MapTextures_LoadMapSlots.md) | V | Map textures from RefinedBgTexture, only for map ids up to 127. |
| <a id="8"></a>8 | [MapAnim_Load](../functions/MapAnim_Load.md) | V | The anim file, when RefinedBgAnim has no row or only rows whose kind is not 0; header tag and map id checked like the mesh. |
| <a id="9"></a>9 | [MapMesh_ApplyPolygonRows](../functions/MapMesh_ApplyPolygonRows.md) | V | Every frame, while the mesh set holds an id: the polygon override rows (with their condition rows) are applied when the battle state value changed. |

## Behavior

- V: the data of stock map 5 (eight texture rows over four slots, eight system rows, one zero anim row, six node rows, one zero polygon row) matches the files of its texture folder and the absence of an anim file.

## Open questions

None recorded.
