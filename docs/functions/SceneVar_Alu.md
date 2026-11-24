# SceneVar_Alu

- **Address:** `0x140242700`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t SceneVar_Alu(int op, int dst, int src, int64_t extra, char flag)`
- **Callers:** SceneVar_Read, SceneVar_Write, EventScript_Run
- **Callees:** SceneVar_ResolveSlot, SceneVar_Read, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The second task group's event variable arithmetic unit. The event interpreter calls it directly to carry out the variable opcodes 0xB0 to 0xBE.

## Behavior

- V: the same arithmetic as EventVar_Alu: even operations use `src` as a literal, odd ones read a variable, variable 33 is the 16-bit random source (`seed * 25173 + 13849`), and operations 176 to 190 are add, subtract, multiply, divide, modulo, AND, OR and clear.
- V: the same write-lock rules and constants (960, 508 and the 0xC test), using SceneVar_Read for the lock check and SceneVar_ResolveSlot to find the storage.
- V: errors (divide by zero, variable id of 1024 or more) call SceneTask_Terminate instead of EventTask_Terminate.
- V: takes two extra arguments compared with the first-group copy.
- V: called by SceneVar_Read, SceneVar_Write and directly by EventScript_Run.

## State touched

- Calls: [SceneVar_ResolveSlot](SceneVar_ResolveSlot.md), [SceneVar_Read](SceneVar_Read.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Called by: [EventScript_Run](EventScript_Run.md), [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md)
- Called by event opcodes: [0xB0](../opcodes/README.md), [0xB1](../opcodes/README.md), [0xB2](../opcodes/README.md), [0xB3](../opcodes/README.md), [0xB4](../opcodes/README.md), [0xB5](../opcodes/README.md), [0xB6](../opcodes/README.md), [0xB7](../opcodes/README.md), [0xB8](../opcodes/README.md), [0xB9](../opcodes/README.md), [0xBA](../opcodes/README.md), [0xBB](../opcodes/README.md), [0xBC](../opcodes/README.md), [0xBD](../opcodes/README.md), [0xBE](../opcodes/README.md)
- Resolves registries: [EventVariables](../registries/EventVariables.md)

## Notes

The operation numbers 176 to 190 are the event opcodes 0xB0 to 0xBE, so the interpreter can pass the opcode straight through.

## Open questions

What the two extra arguments do.
