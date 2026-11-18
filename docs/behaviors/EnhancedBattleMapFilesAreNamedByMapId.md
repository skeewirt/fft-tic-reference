# EnhancedBattleMapFilesAreNamedByMapId

- **Kind:** observed behaviour
- **Scope:** engine (enhanced renderer map load)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Map_LoadBattleData](../functions/Map_LoadBattleData.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The enhanced renderer loads the battle map's mesh and animation by file name built from the map id (three digits at least), and reads one row of the data table 'Map' (registry table 60, keys 0..128) by the map id for camera and render settings.

## Behavior

- V: the mesh path is 'bg/meshes/map_%03d_mesh.bin' and the animation path 'bg/anims/map_%03d_anim.bin' (format strings in the load functions, called with the map id).
- V: the settings row is found by NxdTable_GetRowById(table 60, map id); when no row exists the settings step is skipped, so the previous values stay.
- V: the table 'Map' has 129 rows (ids 0..128) and seven columns; I: the cells hold per-variant render parameters (a record of 72 bytes per variant, indexed by the scene variant); ? the meaning of the cells.
- V: a map id of 15 or 33 skips the mesh load (compared by immediate in the load task).

## Notes

These files are read in the enhanced mode only; the map block and the resource files are read in both modes.

## Open questions

? what the renderer does when the mesh file for the id does not exist; ? the textures path of a map.
