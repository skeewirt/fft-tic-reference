# EventScript_InstructionLength

- **Address:** `0x1402CBE2C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t EventScript_InstructionLength(const uint8_t *instruction)`
- **Callers:** EventScript_FindOpcode, EventScript_FindInstruction, `sub_14023A868`, `sub_140234E04`, `sub_1402358C8`, `sub_140235D38`, `sub_1402404CC`, `sub_1401DEC14`, `sub_1402CBE70`
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the length in bytes of the event script instruction at a pointer: one opcode byte plus its operand bytes.

## Behavior

- V: opcode 0xE6 is variable length: the byte after it is the operand length, so the instruction is that value plus 2 bytes.
- V: every other opcode uses a 256-entry operand-length byte table at 0x140680F00 (image base + 0x680F00) indexed by the opcode: length = table[opcode] + 1.
- V: when the enhanced-edition flag `dword_1407D453C` is 1 three opcodes are longer than the table says: 0x10 (DisplayMessage) by 3 bytes, 0x51 (ChangeDialog) by 2 and 0xEB by 4.
- V: the table holds the original (classic) lengths, for example 14 for opcode 0x10, 5 for 0x51 and 0 for the end opcode 0xDB; the enhanced differences are applied in code.
- V: about 9 callers, all of which walk or scan the script buffer.

## Referenced by

- Called by: [EventMoveTargets_Rewrite](EventMoveTargets_Rewrite.md), [EventScript_FindInstruction](EventScript_FindInstruction.md), [EventScript_FindOpcode](EventScript_FindOpcode.md), [EventScript_Run](EventScript_Run.md), [EventStateTrack_RunTask](EventStateTrack_RunTask.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md), [sub_1401DEC14](sub_1401DEC14.md)
- Called by event opcodes: [0x10](../opcodes/README.md)
- Reads tables: [EventOperandLengths](../tables/EventOperandLengths.md)

## Notes

Any tool that edits event scripts needs exactly this length rule to step from one instruction to the next.

## Open questions

The meaning of the enhanced-only opcodes; this routine gives their length only.
