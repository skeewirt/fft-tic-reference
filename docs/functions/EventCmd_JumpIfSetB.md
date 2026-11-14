# EventCmd_JumpIfSetB

- **Address:** `0x1402F21D0`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_JumpIfSetB(void)`
- **Callers:** EventCmd_Run through the class table, class 19
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 19: jumps to the byte 10 target when the bit for byte 9 is set in flag table B (dword_140D4CC28).

## Behavior

- V: argument layout: byte 9 is the bit index; byte 10 is the jump value; byte 11 is not read.
- V: the entry sets ecx to 1 and jumps to the body at 0x1402F21DC, which is shared with class 20.
- V: tests bit (byte 9 & 31) of the dword at dword_140D4CC28[byte 9 >> 5].
- V: when the bit is set, it sets bit 1 (2, jump pending), writes byte 10 (zero-extended) to the word at offset 14 of xmmword_141862440, the word EventCmd_Run reads back as the jump value, and returns byte 10.
- V: when the bit is clear, it sets bit 2 (4, continue) and returns the table dword that was read.
- V: the shared body compares the tested bit with ecx and takes the jump when they are equal: ecx is 1 for class 19 and 0 for class 20.

## Notes

The body at 0x1402F21DC is shared with class 20, which enters with ecx set to 0. Byte 9 is a single byte, so bit indexes run 0 to 255; the table size was not checked. The IDA name is still EventCmd_JumpIfSetB; no rename was made. Table A (qword_1411A7028) is tested by class 17 (EventCmd_JumpIfByteFlagSet references it); table B is also referenced by sub_1402F109C.

## Open questions

What table B holds and which code writes it; the table size.
