# EventCmd_JumpIfAbove

- **Address:** `0x1402F2674`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_JumpIfAbove(void)`
- **Callers:** EventCmd_Run through the class table, class 37
- **Callees:** none (no calls)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 37 handler. Continues when the current value V is at most the 16-bit target; otherwise requests a jump.

## Behavior

- V: class 37 argument layout: bytes 9 (low) and 10 (high) form the 16-bit target; byte 11 is the jump value, read only on the jump path.
- V: V is the dword at 0x141862474 (the high dword of qword_141862470) plus the signed 16-bit word at 0x141862452 (offset 2 of xmmword_141862450), clamped to at most 65535 and at least 0.
- V: when V is less than or equal to the target: sets bit 2 (value 4, continue) and returns V.
- V: when V is greater than the target: sets bit 1 (value 2, jump pending), writes byte 11 into the 16-bit word at offset 14 of the command register (the high word of its last dword) and returns byte 11.
- I: byte 11 is the jump destination that the EventCmd_Run loop reads from that word.

## Notes

V is never negative after the clamp, so the compare behaves as unsigned. The word at 0x141862452 is also modified by class 51. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What the dword at 0x141862474 and the word at 0x141862452 count. How the loop consumes the word at offset 14 of the command register.
