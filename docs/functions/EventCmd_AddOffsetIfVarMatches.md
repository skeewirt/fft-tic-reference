# EventCmd_AddOffsetIfVarMatches

- **Address:** `0x1402F2B28`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_AddOffsetIfVarMatches(void)`
- **Callers:** EventCmd_Run through the class table, class 51
- **Callees:** EventVar_Read (reads one event variable by index)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 51 handler: reads event variable 24 and, when it equals byte 11, adds bytes 9 and 10 plus 0x8000 to the word at 0x141862452.

## Behavior

- V: argument layout: bytes 9 and 10 form a 16-bit value (byte 9 low); byte 11 is the value compared with event variable 24.
- V: calls EventVar_Read with 0x18 (24).
- V: when that value equals byte 11, adds (the 16-bit value from bytes 9 and 10 minus 0x8000, in 16 bits, which equals plus 0x8000) to the 16-bit word at 0x141862452.
- V: when it does not equal byte 11, the word at 0x141862452 is not changed.
- V: sets bit 2 (value 4, continue). Returns the value read from event variable 24 (replaced by the added value when they match).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md)

## Notes

The 0x8000 offset is read from the code. The word at 0x141862452 is the one class 37 adds to its comparison value. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What event variable 24 is; what the word at 0x141862452 is used for; the meaning of the 0x8000 offset.
