# MapMesh_ApplyPolygonRows

- **Address:** `0x1400C9DCC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapMesh_ApplyPolygonRows(void *meshSet, int stateValue)`
- **Callers:** CharaRenderer_Update
- **Callees:** NxdTable_GetSetEntries, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the per-polygon override arrays from the RefinedBgMeshPolygon rows of the loaded map whenever the battle state value or the loaded map changed.

## Behavior

- V: runs from CharaRenderer_Update only while the mesh set holds a map id; the state value is the battle state's value in states 52, 58 and 59, else -1.
- V: clears the override arrays, takes the whole row set of the map, and for each row follows its condition id into RefinedBgMeshPolygonCond; a row whose condition does not apply, or whose condition row is absent, writes nothing; an applying row writes its 16-bit value into the array chosen by its kind code at its index of its layer.

## State touched

- Calls: [NxdTable_GetSetEntries](NxdTable_GetSetEntries.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md)

## Open questions

?: what each kind code's array does to the drawing.
