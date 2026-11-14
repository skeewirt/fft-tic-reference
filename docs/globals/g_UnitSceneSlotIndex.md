# g_UnitSceneSlotIndex

- **Kind:** global
- **Address:** `0x140822DAC`
- **Type:** `int32[21]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scene-unit slot of each battle unit by its unit index (+444), -1 none: written by sub_14026EB74 (a slot taken by another unit clears that unit's entry) and sub_14026A048, cleared by sub_140210AF0, read on the resume path; inside the battle snapshot region.

## Referenced by

- Described by tables: [UnitSceneSlotIndex](../tables/UnitSceneSlotIndex.md)
- Read by: [sub_14026EB74](../functions/sub_14026EB74.md)
- Written by: [sub_140210AF0](../functions/sub_140210AF0.md), [sub_14026EB74](../functions/sub_14026EB74.md)

## Open questions

None recorded.
