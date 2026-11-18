# MapMesh_InitNodeFlags

- **Address:** `0x1400C89F0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapMesh_InitNodeFlags(void *meshSet)`
- **Callers:** MapMesh_Load, MapRenderer_ReuseLoadedMesh
- **Callees:** MapMesh_StockNodeOffset, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the 32 node slots of the mesh set to their start flags from the node rows, marks the nodes the mesh references, and applies the per-map stock offsets.

## Behavior

- V: every slot starts with two flag bits set and no invisibility values; slot k takes the k-th node row (by position): start-visible bit from +20, two flag bits from +23 and +24, and the two 16-bit values of the RefinedBgMeshNodeInvisType row named by +16.
- V: every node index below 32 found in the mesh's per-layer index arrays is marked used; a used node with no row gets the visible bit set.
- V: the last loop stores MapMesh_StockNodeOffset's answer per node.

## State touched

- Calls: [MapMesh_StockNodeOffset](MapMesh_StockNodeOffset.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Called by: [MapMesh_Load](MapMesh_Load.md), [MapRenderer_ReuseLoadedMesh](MapRenderer_ReuseLoadedMesh.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md)

## Open questions

None recorded.
