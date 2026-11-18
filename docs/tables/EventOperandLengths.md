# EventOperandLengths

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140680F00`
- **Rows:** 256 rows of 1 byte
- **Keyed by:** event script opcode byte
- **Read by:** [EventScript_InstructionLength](../functions/EventScript_InstructionLength.md)
- **Row layout:** [EventOperandLengthRow](../structs/EventOperandLengthRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Operand byte count of every event script opcode; the instruction length reader and three other event functions use it.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
