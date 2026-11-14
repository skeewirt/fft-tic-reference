# EventCmd_JumpIfNotEqual

- **Address:** `0x1402F25D4`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_JumpIfNotEqual(void)`
- **Callers:** EventCmd_Run through the class table, class 35
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 35 handler. Compares the current value V with a 16-bit target from the argument bytes; it continues when they are equal and requests a jump when they differ.

## Behavior

- V: class 35 argument layout: the 16-bit target is byte 9 (low) and byte 10 (high). Byte 11 is the jump value and is read only on the jump path.
- V: V is the high dword of qword_141862470 plus the signed 16-bit word at offset 2 of xmmword_141862450, clamped to the range 0 to 65535 (a negative sum becomes 0).
- V: when V equals the target: sets bit 2 (value 4, continue) and returns V.
- V: when V differs from the target: sets bit 1 (value 2, jump pending), writes byte 11 into the word at offset 14 of xmmword_141862440 (the jump value), and returns byte 11.
- V: EventCmd_Run, when bit 1 is set, adds the signed word at offset 14 to word_140D8DBA4 shifted left 8 to form the new position, then sets status to (AND 0xFFF9) OR 4.

## Notes

Same as EventCmd_JumpIfEqual with the branches swapped.

## Open questions

Same as EventCmd_JumpIfEqual: the source of V.
