# MapMesh_FindNodeRows

- **Address:** `0x1400D5934`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `unsigned MapMesh_FindNodeRows(NodeRowSpan *out, unsigned mapId, unsigned variation)`
- **Callers:** MapMesh_Load
- **Callees:** NxdSets_Find3, NxdSet3_FindChild, NxdTable_GetEntryByKeys3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the RefinedBgMeshNode rows of one map and variation: a pointer to the first row and the row count (0, 0 when there are none).

## Behavior

- V: reads the table by id 153 (cached); needs a triple-keyed table; searches the file's set index for the map, then the child set for the variation, then the first row through the three keys.

## State touched

- Calls: [NxdSets_Find3](NxdSets_Find3.md), [NxdSet3_FindChild](NxdSet3_FindChild.md), [NxdTable_GetEntryByKeys3](NxdTable_GetEntryByKeys3.md)

## Referenced by

- Called by: [MapMesh_Load](MapMesh_Load.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md)

## Open questions

None recorded.
