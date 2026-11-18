# MapRenderer_ReuseLoadedMesh

- **Address:** `0x1400D55C4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapRenderer_ReuseLoadedMesh(void *renderer, int mapId)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** MapMesh_InitNodeFlags

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Re-runs the node setup of an already loaded mesh set (a second battle on the same map).

## Behavior

- V: with the mesh set's id at none it re-initialises the nodes; for id 64 it also sets one flag bit on three nodes; then it reapplies the anim set's table when the anim is loaded.

## State touched

- Calls: [MapMesh_InitNodeFlags](MapMesh_InitNodeFlags.md)

## Referenced by

- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)

## Open questions

None recorded.
