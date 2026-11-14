# EventBlock_ApplyOperands

- **Address:** `0x1402355E0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventBlock_ApplyOperands(const uint8_t *operands)`
- **Callers:** SceneCallback_Dispatch (mode 1, from the opcode 0x28 case of EventScript_Run) and EventSubScript_RunTask (EventSubScript_RunTask).
- **Callees:** EventRef_ResolveSlot, sub_140272D70 (which calls SceneObject_FindBySlot, sub_14027DDB8 and SceneUnit_ReleasePartner)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The callback installed by opcode 0x28: resolves the unit named by its operands and gives it a 128-byte block, a doubled count and a fixed value, using a block helper.

## Behavior

- V: resolves the id at operand bytes 1 and 2 with EventRef_ResolveSlot, using the low byte of the id as the flag. When the result is 2000 it returns 2000 and does nothing else.
- V: builds a three-word vector: word 0 is operand 3, word 1 is operand 5, word 2 is operand 4 (each a signed byte).
- V: the count is operand 6 plus 256 times operand 7 (unsigned 16-bit).
- V: the scale value is 256 minus 256 times operand 8 (operand 8 shifted left by 8, subtracted from 256).
- V: calls sub_140272D70 with the slot, the vector, the scale value, the slot again and the count. That routine finds the unit node (returns 0 when there is none), calls the block helper sub_14027DDB8 with the scale value, the constant 3, the unit bytes at +136, +137 and +138, the first, third and second vector words, and the constant 1.
- V: when the block helper returns a block, sub_140272D70 copies its 128 bytes into the unit record at +168 through +295, sets the dword at +164 to 0, sets the dword at +68 to twice the count, sets the dword at +72 to 0x2000, calls SceneUnit_ReleasePartner on the node and returns 1.
- V: opcode 0x28 calls this function through SceneCallback_Dispatch mode 1 at the moment the opcode runs, with the address of the instruction's operand 1 as the argument. The opcode does not wait.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [SceneUnit_ReleasePartner](SceneUnit_ReleasePartner.md)

## Referenced by

- Called by event opcodes: [0x28](../opcodes/README.md)

## Notes

The block helper sub_14027DDB8 was not decoded, so what the 128 bytes contain is not stated here.

## Open questions

What sub_14027DDB8 computes and what the 128-byte block at unit +168 is used for.
