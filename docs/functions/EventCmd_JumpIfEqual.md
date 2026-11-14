# EventCmd_JumpIfEqual

- **Address:** `0x1402F2584`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_JumpIfEqual(void)`
- **Callers:** EventCmd_Run through the class table, class 34
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 34 handler. Compares the current value V with a 16-bit target from the argument bytes; on equality it requests a jump, otherwise it continues.

## Behavior

- V: class 34 argument layout: the 16-bit target is byte 9 (low) and byte 10 (high). Byte 11 is the jump value and is read only on the equal path.
- V: V is the high dword of qword_141862470 plus the signed 16-bit word at offset 2 of xmmword_141862450, clamped to the range 0 to 65535 (a negative sum becomes 0).
- V: when V equals the target: sets bit 1 (value 2, jump pending), writes byte 11 into the word at offset 14 of xmmword_141862440 (the jump value), and returns byte 11.
- V: when V differs from the target: sets bit 2 (value 4, continue), leaves the offset-14 word alone, and returns V.
- V: EventCmd_Run, when bit 1 is set, adds the signed word at offset 14 to word_140D8DBA4 shifted left 8 to form the new position, then sets status to (AND 0xFFF9) OR 4.

## Notes

Same comparison shape as classes 35 and 36; only the test differs. V is clamped to 0..65535 and compared with the zero-extended 16-bit target.

## Open questions

What the high dword of qword_141862470 and the word at offset 2 of xmmword_141862450 hold.
