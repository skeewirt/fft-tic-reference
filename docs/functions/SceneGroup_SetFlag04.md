# SceneGroup_SetFlag04

- **Address:** `0x140241F54`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneGroup_SetFlag04(int16_t selector, int32_t set)`
- **Callers:** EventScript_Run at 0x14023D1B5 and 0x14023D298 (opcodes 0x6D and 0x6C, set = 1 and set = 0 in the pseudocode, per the opcode records).
- **Callees:** SceneGroup_ResolveId (SceneGroup_ResolveId), SceneUnit_TestGroupMember (SceneUnit_TestGroupMember), SceneObject_FindBySlot (unit lookup)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The shared body of opcodes 0x6C and 0x6D: sets or clears bit 0x04 of byte +143 of each unit selected by the operand.

## Behavior

- V: copies selector into a local word and calls SceneGroup_ResolveId on it; if that returns 0 the function does nothing more.
- V: loops over keys 0 to 20. For each key, SceneUnit_TestGroupMember returns nonzero when the key is in the group; the key is then in the local word.
- V: for each member, it finds the unit node with SceneObject_FindBySlot. When set is nonzero it sets bit 0x04 of the byte at node+0x8F (143). When set is zero it clears that bit. A missing node is skipped.
- V: the loop stops after the first member when the group mode is 0 (a single unit).
- V: the return value is whatever the last call left in rax; no value is set on purpose.

## State touched

- Calls: [SceneGroup_ResolveId](SceneGroup_ResolveId.md), [SceneUnit_TestGroupMember](SceneUnit_TestGroupMember.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Notes

This is the flag-04 companion of the 0x81 path, which sets bit 0x02 at the same offset +143.

## Open questions

What bit 0x04 at +143 controls in the game.
