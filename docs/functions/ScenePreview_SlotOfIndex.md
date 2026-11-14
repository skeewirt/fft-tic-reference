# ScenePreview_SlotOfIndex

- **Address:** `0x140273090`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t ScenePreview_SlotOfIndex(int index)`
- **Callers:** 13 routines (14 call sites): EventScript_Run (2), EventRef_ResolveSlot, sub_1400CB870, sub_14021F538, sub_14022AA88, sub_140233588, sub_1402346D0, EventUnitBlock_RunTask, sub_140239144, sub_140239294, sub_140240B8C, sub_1402DE204 and sub_140360048.
- **Callees:** None (walks the list itself)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The reverse of ScenePreview_IndexOfSlot: finds the object whose preview index is the given value and returns its slot number.

## Behavior

- V: walks the object list from `qword_140D3A410`, following the next pointer at node +0.
- V: for each node whose pointer at node +328 is not null, it compares byte +444 of that pointer with the argument. The first match gives the slot, which is the low byte of the node key at +8.
- V: returns 0xFFFFFFFF (-1 as a signed 32-bit value) when no node matches.
- V: EventRef_ResolveSlot passes a record index of 0 to 20, or 21 when no record matched. The value is in ECX at the call; the decompiler does not show it as an argument.
- I: the result is the slot of the object that uses the given preview record.

## Referenced by

- Called by: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md), [sub_14022AA88](sub_14022AA88.md), [sub_140233588](sub_140233588.md)
- Called by event opcodes: [0x45](../opcodes/README.md)

## Notes

Pairs with ScenePreview_IndexOfSlot. The decompiled signature shows no argument at the call site in EventRef_ResolveSlot; the value is the loop counter.

## Open questions

Whether more than one object can share a preview index; the function returns the first one found in list order.
