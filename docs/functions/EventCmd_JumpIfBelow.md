# EventCmd_JumpIfBelow

- **Address:** `0x1402F2624`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_JumpIfBelow(void)`
- **Callers:** EventCmd_Run through the class table, class 36
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 36 handler. Continues when the current value V is at least the 16-bit target; otherwise requests a jump.

## Behavior

- V: class 36 argument layout: the 16-bit target is byte 9 (low) and byte 10 (high). Byte 11 is the jump value and is read only on the jump path.
- V: V is the high dword of qword_141862470 plus the signed 16-bit word at offset 2 of xmmword_141862450, clamped to the range 0 to 65535 (a negative sum becomes 0).
- V: when V is greater than or equal to the target: sets bit 2 (value 4, continue) and returns V.
- V: when V is less than the target: sets bit 1 (value 2, jump pending), writes byte 11 into the word at offset 14 of xmmword_141862440 (the jump value), and returns byte 11.
- V: EventCmd_Run, when bit 1 is set, adds the signed word at offset 14 to word_140D8DBA4 shifted left 8 to form the new position, then sets status to (AND 0xFFF9) OR 4.

## Notes

Same shape as classes 34 and 35. The compare is a signed jge on two non-negative values.

## Open questions

Same as EventCmd_JumpIfEqual: the source of V.
