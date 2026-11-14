# EventScript_IsSkipStop

- **Address:** `0x14021F1B4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventScript_IsSkipStop(int opcode, int *flagOut)`
- **Callers:** EventScript_Run
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether a given opcode counts as a stopping point when the interpreter skips forward through a script.

## Behavior

- V: returns true for a fixed set of opcodes and false for all others.
- V: opcodes 0x19, 0x58, 0x59, 0x7F and 0xD0 count only while the current event number `dword_140782A94` is 213, and opcode 0x3D only while it is 2.
- V: opcode 0x78 counts only when `dword_142FF9EBC` is non-zero; opcode 0x76 counts only when that is non-zero and `word_142FEC554` is zero. When either counts it sets `*flagOut` to 1 and clears a field, and 0x76 also sets `word_142FEC528` to 32.
- V: opcode 0xE5 counts only when `*flagOut` is non-zero, and then clears it.
- V: called twice from EventScript_Run, in loops that step forward with EventScript_InstructionLength until this returns true.
- I: the true opcodes are the ones that must still run, or be noticed, while the player skips a cutscene.

## Referenced by

- Called by: [EventScript_Run](EventScript_Run.md)

## Notes

Named for its use in the skip loops; the opcode set itself is a decision table in the code.

## Open questions

Confirm the skip behavior against a running skip, and name the state words.
