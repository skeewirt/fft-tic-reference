# EventCmd_SetJumpTarget

- **Address:** `0x1402F1CDC`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetJumpTarget(void)`
- **Callers:** EventCmd_Run through the class table, class 6
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 6 handler: stores argument byte 9 as a jump target in the status register and sets the jump-pending bit.

## Behavior

- V: sets bit 1 (0x2) of the status word unconditionally.
- V: stores argument byte 9 into the high word (bytes 14-15) of xmmword_141862440.
- V: returns argument byte 9.
- V: bytes 10 and 11 are not used, and bits 2, 3 and 5 are not set.

## Notes

The value stored is the same one returned; the caller reads it from the register or the return value (not traced).

## Open questions

Whether EventCmd_Run reads the target from the high word of xmmword_141862440 after a jump-pending result (not traced).
