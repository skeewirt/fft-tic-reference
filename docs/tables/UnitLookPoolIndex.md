# UnitLookPoolIndex

- **Kind:** table
- **Storage:** Executable (filled at run time)
- **Rows:** 21 entries of 4 bytes
- **Held in:** [g_UnitLookPoolIndex](../globals/g_UnitLookPoolIndex.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Look pool index of each battle unit by its unit index (+444): written by SceneUnit_BuildFromQueueEntry when it builds the unit's scene unit, read back by it on the resume path (load mode 1) and by sub_1401D46B0; inside the battle snapshot region at 0x1408167A0.

## Open questions

None recorded.
