# UnitSceneSlotIndex

- **Kind:** table
- **Storage:** Executable (filled at run time)
- **Rows:** 21 entries of 4 bytes
- **Held in:** [g_UnitSceneSlotIndex](../globals/g_UnitSceneSlotIndex.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scene-unit slot of each battle unit by its unit index (+444), -1 none: written by SceneUnit_BuildFromQueueEntry (a slot taken by another unit clears that unit's entry) and sub_14026A048, cleared by sub_140210AF0, read on the resume path; inside the battle snapshot region.

## Open questions

None recorded.
