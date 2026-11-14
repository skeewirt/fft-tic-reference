# g_StatusGroupMasks

- **Kind:** global
- **Address:** `0x1411A6A70`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[10][5]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The ten party-wide status group masks, five bytes each: a group test ANDs these bytes against the unit status bytes at +0x61..+0x65.

## Behavior

- V: built once by Status_BuildFlagMasks and read by Unit_HasStatusGroup.

## Referenced by

- Described by tables: [StatusGroupMasks](../tables/StatusGroupMasks.md)
- Read by: [Unit_HasStatusGroup](../functions/Unit_HasStatusGroup.md)

## Open questions

None recorded.
