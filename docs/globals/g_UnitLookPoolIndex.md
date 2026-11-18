# g_UnitLookPoolIndex

- **Kind:** global
- **Address:** `0x140822D58`
- **Type:** `int32[21]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Look pool index of each battle unit by its unit index (+444): written by SceneUnit_BuildFromQueueEntry when it builds the unit's scene unit, read back by it on the resume path (load mode 1) and by sub_1401D46B0; inside the battle snapshot region at 0x1408167A0.

## Referenced by

- Described by tables: [UnitLookPoolIndex](../tables/UnitLookPoolIndex.md)
- Read by: [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md)
- Written by: [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md)

## Open questions

None recorded.
