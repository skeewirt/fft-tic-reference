# EventCmd_SetFlagA

- **Address:** `0x1402F2230`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_SetFlagA(void)`
- **Callers:** EventCmd_Run through the class table, class 21
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 21: sets the flag bit named by byte 9 in flag table A (qword_1411A7028), the table that classes 17 and 18 test.

## Behavior

- V: argument layout: byte 9 is the bit index (0 to 255); bytes 10 and 11 are not read.
- V: sets bit 2 (4, continue) of the status word.
- V: sets bit (byte 9 & 31) in the dword at qword_1411A7028 + 4 * (byte 9 >> 5), leaving other bits unchanged.
- V: returns the mask 1 << (byte 9 & 31).

## Notes

This is the only handler in this set that writes table A; classes 17 and 18 read it. The IDA name is still EventCmd_SetFlagA; no rename was made.

## Open questions

The overlap of table A with dword_1411A7030 (used by classes 15 and 16) and whether that overlap is intended; what sets table A outside this handler.
