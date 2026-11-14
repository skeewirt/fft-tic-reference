# EventUnitStatus_SetBit

- **Address:** `0x140241BD0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventUnitStatus_SetBit(int64_t ref, int bit, int flag)`
- **Callers:** EventUnitStatus_ApplyTask (eight call sites, 0x1402419BB to 0x140241B0B). A data reference at 0x143D384B8 was not traced.
- **Callees:** EventRef_ResolveSlot, ScenePreview_IndexOfSlot, SceneCallback_Dispatch (sub_14030C87C is set as the callback and not called here)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For one unit reference, clears two 5-byte bitmaps in the unit's preview row, sets one bit in one of them, and sends mode 2 of the scene callback dispatch for that row.

## Behavior

- V: resolves ref with EventRef_ResolveSlot, passing the bit number as the flag argument (that routine does not use it). Returns with no change when the result is 2000.
- V: takes ScenePreview_IndexOfSlot of the slot. Returns with no change when the index is -1 or 2000.
- V: for an index from 0 to 20 the row is g_BattleUnitTable plus 512 times the index. For an index from 21 to 255 the row pointer is set to null, and the stores below then go through that null pointer (not confirmed by a run).
- V: clears the five bytes at row +475 to +479 and the five bytes at row +480 to +484.
- V: sets bit number bit in a bitmap: byte (bit divided by 8) of the first bitmap at row +475 when flag is not zero, or of the second bitmap at row +480 when flag is zero. The bit value is 1 shifted by (bit modulo 8).
- V: sets the callback qword_140D40940 to sub_14030C87C and returns the result of SceneCallback_Dispatch with mode 2, the index, argument 1 and two zeros.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md), [SceneCallback_Dispatch](SceneCallback_Dispatch.md)

## Referenced by

- Called by: [EventUnitStatus_ApplyTask](EventUnitStatus_ApplyTask.md)

## Notes

The bitmaps are read by the mode 2 callback sub_14030C87C, which was not traced.

## Open questions

What the two 5-byte bitmaps at row +475 and +480 mean and what the callback does with them; what the null row pointer does for indexes 21 to 255 (the code writes through it).
