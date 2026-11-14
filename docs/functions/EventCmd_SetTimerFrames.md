# EventCmd_SetTimerFrames

- **Address:** `0x1402F29B8`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetTimerFrames(void)`
- **Callers:** EventCmd_Run through the class table, class 46
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 46 handler: stores a byte in dword_140D4CC10, sets dword_140D8DBA8 to 60 times a 16-bit count, clears dword_140D4CA04, and returns byte 11.

## Behavior

- V: argument layout: bytes 9 and 10 form a 16-bit count (byte 9 is the low byte, byte 10 the high byte); byte 11 is the value stored in dword_140D4CC10 and the return value.
- V: sets dword_140D4CA04 to 0.
- V: sets dword_140D4CC10 to byte 11.
- V: sets dword_140D8DBA8 to 60 * (the 16-bit count from bytes 9 and 10).
- V: sets bit 2 (value 4) of the status word (continue). Returns byte 11.

## Notes

The multiplier 60 is read from the code; the unit it converts to is inferred (I: frames at 60 per second).

## Open questions

What dword_140D4CA04, dword_140D4CC10 and dword_140D8DBA8 are used for; whether the multiplier is frames per second as inferred.
