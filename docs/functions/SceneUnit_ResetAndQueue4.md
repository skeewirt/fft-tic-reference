# SceneUnit_ResetAndQueue4

- **Address:** `0x140270864`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_ResetAndQueue4(int16_t key, int32_t arg2, int16_t arg3, int16_t arg4, int16_t arg5)`
- **Callers:** EventScript_Run at 0x14023DE52 (inside a loop over 21 slots that compares byte +401 of each preview entry with the operand, with arguments slot, 2, -31, -31, 0; matches opcode 0x99 per the record); EventScript_Run at 0x14023C2E0 (same argument pattern, opcode not confirmed); sub_140240A78 (opcode 0x94 helper, at 0x140240B24 with +31 and at 0x140240B4C with -31); sub_14020435C and sub_14026A048 (other helpers).
- **Callees:** SceneObject_FindBySlot (unit lookup), sub_140260AEC (move to front), sub_1402F7C20 (queued action, not read in full)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets a unit's state bytes and words and queues an action (code 4) with the given values through sub_1402F7C20. Used by the opcode 0x94 and 0x99 paths.

## Behavior

- V: calls SceneObject_FindBySlot(key) to get the unit node. If there is none, it returns 0 and does nothing else.
- V: calls sub_140260AEC(key), which moves the node to the front of the unit list at qword_140D3A410 and returns 1 when it finds the node.
- V: clears bit 0x20 and sets bit 0x10 of the byte at node+0x12C.
- V: clears bit 0x40 and sets bits 0x21 of the word at node+0x18.
- V: sets the byte at node+0x318 to 1.
- V: calls sub_1402F7C20(4, arg2, key, arg3, arg4, arg5). The value 4 is passed by value. sub_1402F7C20 applies the action to slot key when key is below 16, and to all 16 slots (indices 0 to 15) when key is 16 or more.
- V: sets the dword at node+0x80 to 0, the word at node+0x12 to 0xFFFF and the byte at node+0x156 to 0.
- V: returns 0.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [SceneUnit_Oscillate120](SceneUnit_Oscillate120.md), [sub_14020435C](sub_14020435C.md)
- Called by event opcodes: [0x94](../opcodes/README.md)

## Notes

The arguments arg3 and arg4 are the +31 and -31 values that opcode 0x94 passes through sub_140240A78.

## Open questions

What arg2, arg3, arg4 and arg5 mean inside sub_1402F7C20 (not traced), and what the flags at node+0x12C, +0x18 and +0x318 control.
