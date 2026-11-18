# MapTextures_Reset

- **Address:** `0x1400CA95C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MapTextures_Reset(void *textureSet)`
- **Callers:** MapRenderer_ApplyMapRow, MapBlock_ApplyLayerCommand
- **Callees:** sub_1403CAEA4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases every map and system texture of the texture set and sets its id fields to none.

## Behavior

- V: for 21 slots x 201 frames releases the texture handle unless it is a shared copy; releases the 8 system handles; the map id, texture-source and variation fields become -1 or 0.

## Referenced by

- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md), [MapRenderer_ApplyMapRow](MapRenderer_ApplyMapRow.md)

## Open questions

None recorded.
