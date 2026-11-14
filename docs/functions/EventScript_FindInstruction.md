# EventScript_FindInstruction

- **Address:** `0x1402425D0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t EventScript_FindInstruction(int offset, int opcode, int altOpcode, int argByte)`
- **Callers:** `sub_14023A868`
- **Callees:** EventScript_InstructionLength, `sub_1402F7EC8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scans the loaded event script for an instruction with a given opcode (or an alternative opcode) whose first operand byte has a given value.

## Behavior

- V: for any opcode other than 0xD5 it walks instruction by instruction from `offset` until the end opcode 0xDB; a match is an instruction whose opcode equals `opcode`, or equals `altOpcode` when that is not -1, and whose first operand byte equals `argByte`.
- V: a match returns the match's offset plus 2.
- V: when the end opcode is reached with no match it calls `sub_1402F7EC8` and returns 0.
- V: opcode 0xD5 takes a different path: it walks the instructions from the start of the script up to `offset` and returns a position derived from the last one passed.
- I: opcode 0xD5 is a jump-target style opcode and is searched by position, not by argument.

## State touched

- Calls: [EventScript_InstructionLength](EventScript_InstructionLength.md)

## Referenced by

- Called by: [EventScript_Run](EventScript_Run.md)

## Notes

Used to resolve jump and label targets inside the loaded script.

## Open questions

The exact return value of the 0xD5 path.
