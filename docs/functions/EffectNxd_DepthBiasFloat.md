# EffectNxd_DepthBiasFloat

- **Address:** `0x1400D2D6C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `float EffectNxd_DepthBiasFloat(int id)`
- **Callers:** CharaRenderer_Init, EffectNxd_LoadRow, MapRenderer_ApplyMapRow, sub_1403CDA40
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the depth bias float of a DepthBias table row.

## Behavior

- V: reads the DepthBias table row (table 315) of the id and returns its +4 as a float.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [MapRenderer_ApplyMapRow](MapRenderer_ApplyMapRow.md)

## Notes

Name is ours.

## Open questions

None recorded.
