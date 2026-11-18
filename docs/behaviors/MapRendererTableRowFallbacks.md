# MapRendererTableRowFallbacks

- **Kind:** observed behaviour
- **Scope:** engine (map renderer tables)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapMesh_FindNodeRows](../functions/MapMesh_FindNodeRows.md), [MapMesh_InitNodeFlags](../functions/MapMesh_InitNodeFlags.md), [MapMesh_ApplyPolygonRows](../functions/MapMesh_ApplyPolygonRows.md), [MapTextures_LoadSystemSlots](../functions/MapTextures_LoadSystemSlots.md), [MapTextures_LoadMapSlots](../functions/MapTextures_LoadMapSlots.md), [MapAnim_ReadRows](../functions/MapAnim_ReadRows.md), [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What each renderer table gives the build when a map has no row: nodes get default flags (visible), polygon overrides do nothing, system textures use the stock default file, map textures are an empty set, the anim file is requested, and a missing Map row skips the variation settings but not the mesh load.

## Behavior

- V: node rows are looked up by (map, variation or 0), with a second try on variation 0; none found leaves every referenced node with its default flags and the visible bit set.
- V: polygon rows are the whole set of the map; none means no override; a polygon row whose condition id has no row is skipped.
- V: RefinedBgAnim without a row requests the anim file; a row of kind 0 does not.
- I: the multi-keyed tables are searched through a sorted set index stored in the file, so rows for a new key need set records for that key to be found.

## Open questions

None recorded.
