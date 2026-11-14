# EventCmd_JumpIfVarEqual

- **Address:** `0x1402F1CF4`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_JumpIfVarEqual(void)`
- **Callers:** EventCmd_Run through the class table, class 7
- **Callees:** sub_1402F1D00 (calls EventVar_Read with 24)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 7 handler: jumps (sets jump-pending with the target byte) when event variable 24 equals argument byte 10, and continues otherwise.

## Behavior

- V: the handler address is a two-instruction stub: it sets ecx to 1 and jumps to sub_1402F1D00.
- V: sub_1402F1D00 reads argument byte 10, calls EventVar_Read(24), and tests (byte 10 equals the variable) against its parameter (1 for class 7, 0 for class 8).
- V: when the test matches: sets bit 1 (0x2), stores argument byte 9 into the high word (bytes 14-15) of xmmword_141862440, and returns byte 9.
- V: when the test does not match: sets bit 2 (0x4) and returns the EventVar_Read result.
- V: bit 3 and bit 5 are not set here.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md)

## Notes

This is the equal-test form of the conditional jump; class 8 is the not-equal form using the same helper.

## Open questions

What event variable 24 holds; what the caller does with the jump target in the high word of xmmword_141862440.
