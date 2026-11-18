# MapTextures_SlotVariantCode

- **Address:** `0x1400CACDC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MapTextures_SlotVariantCode(void *textureSet, int slot, int type)`
- **Callers:** MapTextures_LoadMapSlots
- **Callees:** NxdTable_GetEntryByKeys3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the per-variation integer of a texture row minus one (0 when the entry is 0 or the row is absent).

## Behavior

- V: reads the row (map id, slot, type) and the integer array at the variation or kind index; only when the texture-source field is 0.

## State touched

- Calls: [NxdTable_GetEntryByKeys3](NxdTable_GetEntryByKeys3.md)

## Referenced by

- Called by: [MapTextures_LoadMapSlots](MapTextures_LoadMapSlots.md)

## Open questions

None recorded.
