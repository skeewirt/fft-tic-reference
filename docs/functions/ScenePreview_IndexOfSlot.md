# ScenePreview_IndexOfSlot

- **Address:** `0x140273064`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t ScenePreview_IndexOfSlot(int16_t slot)`
- **Callers:** 21 routines (30 call sites): EventScript_Run (10), EventRef_ResolveSlot, EventMessage_Task, sub_140221C00, sub_140222740, sub_140214284, sub_1402356B0, sub_140240A78, sub_1402416C8, EventUnitStatus_ApplyTask, sub_140241BD0, sub_140241CB0, sub_1402D9490, sub_1402D9F4C, sub_1402DE204 and sub_1402DE418, among others.
- **Callees:** SceneObject_FindBySlot

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the preview index of the object in a slot: byte +444 of the object's preview data, or -1 when the slot has no object or no preview data.

## Behavior

- V: calls SceneObject_FindBySlot(slot). When the node exists and the pointer at node +328 is not null, it returns the byte at that pointer +444, a value from 0 to 255.
- V: otherwise it returns 0xFFFFFFFF, which is -1 as a signed 32-bit value. EventRef_ResolveSlot and EventScript_Run test for that value.
- V: callers use the result as a record index into g_BattleUnitTable (512 bytes per record), for example `g_BattleUnitTable + 512 * result` in EventRef_ResolveSlot.
- I: the preview index is the record number in g_BattleUnitTable for the object.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [EventPreviewUnit_StageSlot](EventPreviewUnit_StageSlot.md), [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [EventUnitStatus_ApplyTask](EventUnitStatus_ApplyTask.md), [EventUnitStatus_RunMembers](EventUnitStatus_RunMembers.md), [EventUnitStatus_SetBit](EventUnitStatus_SetBit.md), [SceneUnit_Oscillate120](SceneUnit_Oscillate120.md), [SceneUnit_TestGroupMember](SceneUnit_TestGroupMember.md), [SceneUnit_ZeroPosAndReset](SceneUnit_ZeroPosAndReset.md)

## Notes

Its inverse is ScenePreview_SlotOfIndex.

## Open questions

What the object's preview data at node +328 is, and what byte +444 holds beyond its use as a record index.
