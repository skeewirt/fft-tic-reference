# EventMoveTargets_Rewrite

- **Address:** `0x1402404CC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int16_t EventMoveTargets_Rewrite(uint8_t *operands, char flag)`
- **Callers:** EventScript_Run (opcode 0x1F case, after EventAngle_Quantize) and EventStateTrack_RunTask (EventStateTrack_RunTask).
- **Callees:** EventScript_InstructionLength, EventRef_ResolveSlot, sub_1402269C0, sub_140272D28, sub_140249088

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rewrites the operands of the next opcode 0x19 from the vectors of two units and, in mode 0, adds an angle target equal to the current angle plus the shortest turn to a fixed angle table.

## Behavior

- V: reads the first id from operand bytes 1 and 2, the second id from operand bytes 3 and 4, and the mode byte from operand 5.
- V: scans forward from the byte after the instruction, step by step with EventScript_InstructionLength, until it finds opcode byte 0x19. The scan has no bound in the code. The operands of that instruction are the target.
- V: resolves both ids with EventRef_ResolveSlot. When either result is 2000, it writes 0xC0 over the 0x19 opcode byte and does nothing else.
- V: otherwise it calls sub_1402269C0 for each slot. That routine copies three signed 16-bit words from the unit node at +76, +78 and +80 into a three-dword buffer, one buffer per unit. It writes nothing when the node is missing.
- V: the three targets are 16-bit words at the 0x19 operand bytes 0-1 (x), 2-3 (y) and 4-5 (z). Each is twice the sum of the two units' values for that component.
- V: the y component of each unit gets +32 before the sum. When the raw first id is 73 each unit's y gets a further -80; when the raw second id is 65 each unit's y gets a further -32.
- V: the x and z sums use the raw unit values with no adjustment.
- V: mode byte 0 only: the code also writes an angle target at the 0x19 operand bytes 8-9 (the word after the 6 target bytes). Other mode values write only the three position targets.
- V: in mode 0 the current angle is the 12-bit value (dword at +120, masked with 0xFFF) of the record at the global pointer off_1407830D8; the 16-bit word at +120 of that record is the base of the angle target.
- V: for each unit, the three bytes at unit node +136, +137 and +138 form an index: byte 136 plus byte 137 times the byte at byte_140C6AD6A plus 256 times byte 138. That index selects an 8-byte entry of byte_140D8DCB0; the low four bits of byte +7 of the entry (mode 11 of sub_140249088) form a mask. The two units' masks are OR-ed.
- V: the table has four 16-bit angles at unk_140672100 to 140672107. Entry j is skipped when bit j of the OR-ed mask is set.
- V: for each remaining entry it computes the signed difference from the current angle and the shorter circular distance in 4096 units; the entry with the smallest distance wins, with ties going to the lower index. The distance starts at 32768 and the direction at +1; when every entry is skipped the target is the base plus 32768.
- V: the angle target is the base word plus the direction times the distance, written as a 16-bit value. The direction is +1 or -1, and the function returns it in mode 0.
- V: in modes other than 0 the return value is the high byte of the last position target written; how the interpreter uses it was not checked.
- V: the function does not wait, and it does not change the 0x19 opcode byte when both ids resolve.

## State touched

- Calls: [EventScript_InstructionLength](EventScript_InstructionLength.md), [EventRef_ResolveSlot](EventRef_ResolveSlot.md)

## Notes

The second argument is passed as the reference flag to EventRef_ResolveSlot; for the second id the code does not set that register, so it carries the value left by the first call.

## Open questions

What byte_140C6AD6A holds; what the four table angles are; what the 0x19 targets mean to the 0x19 handler; why the decompiler shows the second flag as unset.
