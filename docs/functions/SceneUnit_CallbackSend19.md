# SceneUnit_CallbackSend19

- **Address:** `0x140273810`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_CallbackSend19(int16_t key)`
- **Callers:** EventScript_Run (opcode 0x98, through the global callback qword_140D40940; the reference is at 0x14023DD25).
- **Callees:** SceneObject_FindBySlot (unit lookup), sub_1401FAE5C (builds and sends the record), sub_140310B64 (not read)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The callback that opcode 0x98 installs in the global qword_140D40940: for one unit key it sends the value 0x13 to the unit's sub-record and returns whether the unit exists.

## Behavior

- V: calls SceneObject_FindBySlot(key) to get the unit node. If there is none, it returns 0.
- V: if there is a node, it calls sub_1401FAE5C(node, 0x13) and returns 1.
- V: sub_1401FAE5C builds a 232-byte local record with the node's key byte (node+8) and a fixed word pattern, then calls sub_140310B64 with the value 0x13 and the sub-record's byte +4, but only when the node's pointer at +0x148 is nonzero; otherwise it returns 0.
- I: the function is stored in a global callback pointer, not called by a fixed name, so the key is the only argument it receives.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [SceneUnit_Oscillate120](SceneUnit_Oscillate120.md)

## Notes

Installed with mode 1 by the opcode 0x98 record (opcode records, data/opcodes.jsonl). The pseudocode line that stores it sits under a label the search read as case 0xC4, which is not what the record says.

## Open questions

What sub_140310B64 does with the value 0x13. The meaning of mode 1 is not seen in this function.
