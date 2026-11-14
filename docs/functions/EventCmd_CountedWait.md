# EventCmd_CountedWait

- **Address:** `0x1402F1D5C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_CountedWait(void)`
- **Callers:** EventCmd_Run through the class table, class 9
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 9 handler: a counted wait. Each call sets the wait bit and advances a counter; once the counter passes the limit, it sets the continue bit instead.

## Behavior

- V: sets bit 3 (0x8) of the status word.
- V: when bit 4 (0x10) of the status word is set on entry, the limit dword_14186243C is set to argument byte 9 and the counter dword_141862438 is reset to 0.
- V: otherwise the stored limit and counter are used as they are.
- V: when the counter is less than or equal to the limit (signed compare), the counter is increased by 1 and the new counter value is returned; the wait bit stays set.
- V: when the counter is greater than the limit, the handler sets bit 2 (0x4), leaves the counter unchanged and returns it. The wait bit stays set.
- V: argument byte 9 is read only in the reset case; bytes 10 and 11 are not used.
- I: the caller re-runs the instruction while the wait bit is set, so the count is the number of waits before the continue.

## Notes

The reset happens only when bit 4 of the status word is set on entry; nothing in this handler sets bit 4.

## Open questions

Which code sets bit 4 (0x10) before this handler; whether the caller re-runs the instruction while bit 3 is set (I: inferred, not checked in EventCmd_Run).
