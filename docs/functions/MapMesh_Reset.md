# MapMesh_Reset

- **Address:** `0x1400CA258`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapMesh_Reset(void *meshSet)`
- **Callers:** MapRenderer_ApplyMapRow
- **Callees:** memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the mesh set: node arrays, layer data and counts.

## Behavior

- V: clears the large arrays, refills the per-layer index blocks with 0xFF, sets the layer count and node state to 0; the loaded-id field is set to its none value by the caller.

## Referenced by

- Called by: [MapRenderer_ApplyMapRow](MapRenderer_ApplyMapRow.md)

## Open questions

None recorded.
