# MapMesh_StockNodeOffset

- **Address:** `0x1400C8D94`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MapMesh_StockNodeOffset(int mapId, int node, float *x, float *y, float *z)`
- **Callers:** MapMesh_Load, MapMesh_InitNodeFlags
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A hard-coded list of position offsets for single nodes of nine stock maps; 0 for every other map and node.

## Behavior

- V: ids above 116 return 0 at once (the stock renderer tables end at 116); for the listed maps and nodes it returns a kind number and fills the three offsets.

## Referenced by

- Called by: [MapMesh_InitNodeFlags](MapMesh_InitNodeFlags.md), [MapMesh_Load](MapMesh_Load.md)

## Open questions

None recorded.
