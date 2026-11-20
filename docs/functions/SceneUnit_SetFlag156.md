# SceneUnit_SetFlag156

- **Address:** `0x14027322C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_SetFlag156(int16_t key)`
- **Callers:** EventScript_Run (opcode 0x46, at the calls near 0x14023B313 to 0x14023C9F5); sub_140210AF0, EventSubScript_RunTask, sub_14026E194 and sub_140273270 (helpers).
- **Callees:** SceneObject_FindBySlot (unit lookup)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks a unit's flag byte at +0x156 as set (0 during event 54) and clears two of its state words. The body of opcode 0x46 on one unit.

## Behavior

- V: calls SceneObject_FindBySlot(key). If there is no unit node it returns 0.
- V: sets the byte at node+0x156 to 1.
- V: reads the current event number dword_140782A94; when it equals 54 (0x36) the byte is set to 0 instead.
- V: clears the word at node+0x0E and the word at node+0x1F8.
- V: returns 1 when the node exists.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [EventSubScript_RunTask](EventSubScript_RunTask.md), [SceneObjects_StepStates](SceneObjects_StepStates.md)
- Called by event opcodes: [0x46](../opcodes/README.md)

## Notes

The byte at +0x156 is the one the opcode record for 0x46 describes as set to 1, with an exception for event 54.

## Open questions

What the byte at +0x156 and the two words at +0x0E and +0x1F8 are read for elsewhere.
