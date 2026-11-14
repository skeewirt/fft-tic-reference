# EventScript_FindOpcode

- **Address:** `0x1402426BC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t EventScript_FindOpcode(uint32_t offset, int opcode)`
- **Callers:** `sub_14023A868`
- **Callees:** EventScript_InstructionLength

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scans the loaded event script from a byte offset for the next instruction with a given opcode and returns its offset.

## Behavior

- V: starts at `offset` in the event buffer pointed to by `qword_140D40A90` and steps instruction by instruction with EventScript_InstructionLength.
- V: returns the offset of the first instruction whose opcode equals the requested one.
- V: the end opcode 0xDB (219) is checked first: reaching it returns 0, so searching for 0xDB itself always returns 0.
- V: used by the event preparation routine `sub_14023A868`, for example to find every 0x92 instruction before the event starts.

## State touched

- Calls: [EventScript_InstructionLength](EventScript_InstructionLength.md)

## Referenced by

- Called by: [EventScript_Run](EventScript_Run.md)
- Called by event opcodes: [0x10](../opcodes/README.md), [0x1D](../opcodes/README.md), [0x2A](../opcodes/README.md), [0x49](../opcodes/README.md)

## Notes

A zero return means not found, which cannot be confused with a real match because instruction offsets that follow a scan start are greater than zero.

## Open questions

None recorded.
