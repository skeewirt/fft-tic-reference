# EventCmd_SetAccumulator

- **Address:** `0x1402F22E8`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetAccumulator(void)`
- **Callers:** EventCmd_Run through the class table, class 25
- **Callees:** sub_1401E02E8 (only when the presence flag is set)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 25 event command: stores a 16-bit value from the argument in the high dword of qword_141862470 and, when the state object is present, passes that value to the state setter sub_1401E02E8.

## Behavior

- V: class_note: argument bytes 9 (low byte) and 10 (high byte) form the 16-bit value. Byte 11 is not stored; it appears only in the return value when the state object is absent.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word.
- V: writes the 16-bit value into the high dword of qword_141862470. The low dword of that global is not changed.
- V: when the dword at +48 of the state object qword_143CD9E28 is non-zero (the presence flag), calls sub_1401E02E8 with the state object and the 16-bit value, and returns its result.
- V: when the presence flag is zero, the return value is the full 24-bit argument (bytes 9 to 11) and nothing else happens.
- V: does not wait.

## Notes

Class 30 writes the same high dword with a clamped sum. Class 28 passes the signed high dword of this global to sub_1401E02E8.

## Open questions

What qword_141862470 represents to the game; the meaning of the value passed to sub_1401E02E8 (its own readers were not traced).
