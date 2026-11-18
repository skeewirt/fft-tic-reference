# g_UnitSceneSlotIndex

- **Kind:** global
- **Address:** `0x140822DAC`
- **Type:** `int32[21]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scene-unit slot of each battle unit by its unit index (+444), -1 none: written by SceneUnit_BuildFromQueueEntry (a slot taken by another unit clears that unit's entry) and sub_14026A048, cleared by sub_140210AF0, read on the resume path; inside the battle snapshot region.

## Referenced by

- Described by tables: [UnitSceneSlotIndex](../tables/UnitSceneSlotIndex.md)
- Read by: [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md)
- Written by: [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [sub_140210AF0](../functions/sub_140210AF0.md)

## Open questions

None recorded.
