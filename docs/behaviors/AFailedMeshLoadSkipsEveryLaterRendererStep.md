# AFailedMeshLoadSkipsEveryLaterRendererStep

- **Kind:** observed behaviour
- **Scope:** engine (map renderer)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapBlock_ApplyLayerCommand](../functions/MapBlock_ApplyLayerCommand.md), [MapMesh_Load](../functions/MapMesh_Load.md), [MapAnim_Load](../functions/MapAnim_Load.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

When MapMesh_Load returns anything but 0 (missing file, oversize, wrong header, ids 15 and 33) the texture, system-texture and anim steps are not run and the mesh set's loaded-id field stays at none; the map block's tile and polygon records are still applied.

## Behavior

- V: the caller tests the result right after the call; only 0 leads to the texture reset, the id fields, the two texture loaders and the anim load.
- V: with the loaded-id field at none, the polygon rebuild and the node timers do nothing.
- I: the stock pack has RefinedBgTexture rows for maps 42, 97..99, 101 and 102 with no mesh file and no texture folder, which fits a silent skip.
- ?: what draws the sky gradient and the black deployment view when no mesh is loaded.

## Open questions

None recorded.
