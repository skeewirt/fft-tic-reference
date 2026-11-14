# ScenePreview_ClaimForUnit

- **Address:** `0x1402731E8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t ScenePreview_ClaimForUnit(int16_t key)`
- **Callers:** EventScript_Run (opcode 0x45 path, at the calls near 0x14023B208 to 0x14023CA9F); sub_1402029DC, EventSubScript_RunTask, EventUnitBlock_RunTask and sub_140269DC4 (helpers).
- **Callees:** SceneObject_FindBySlot (unit lookup), sub_1402718CC (claim a preview entry)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For one unit: sets its state words at +0x0E and +0x1F8 to 1 and claims its preview entry. Used by opcode 0x45 on the unit side.

## Behavior

- V: calls SceneObject_FindBySlot(key). If there is no unit node it returns 0.
- V: sets the words at node+0x0E and node+0x1F8 to 1.
- V: reads the node's sub-record pointer at +0x148. When it is nonzero, it reads the byte at sub-record +0x1BC (the preview index) and calls sub_1402718CC with that index.
- V: returns 1 when the node exists.
- V: sub_1402718CC(index) does this: when the entry's owner byte (+1) is 0xFF (free), it returns -1 if byte +437 is nonzero; otherwise it stores index in the owner byte, sets byte +437 to 1, and, if the entry's byte +5 has bits 0x30 set, adds the entry's byte +41 to word_14114B0B4 and raises byte_140D405A2 to it when larger. When the owner byte is not 0xFF it does nothing and returns 0.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [Battle_TurnStep](Battle_TurnStep.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md)
- Called by event opcodes: [0x44](../opcodes/README.md), [0x45](../opcodes/README.md)

## Notes

The brief calls this the release side of opcode 0x45; in the code it claims the entry (writes the slot into the owner byte), and the release is not in this function.

## Open questions

Where the owner byte at entry +1 is cleared again (the release path, not traced). What word_14114B0B4 and byte_140D405A2 hold.
