# EventCmd_JumpIfByteFlagSet

- **Address:** `0x1402F2170`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_JumpIfByteFlagSet(void)`
- **Callers:** EventCmd_Run through the class table, class 17
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 17: jumps to the byte 10 target when the bit for byte 9 is set in the flag table at qword_1411A7028 (a flag indexed by one byte).

## Behavior

- V: argument layout: byte 9 is the bit index (0 to 255); byte 10 is the jump value; byte 11 is not read.
- V: the entry sets ecx to 1 and jumps to the shared body at 0x1402F217C.
- V: tests bit (byte 9 & 31) of the dword at qword_1411A7028 + 4 * (byte 9 >> 5).
- V: when the bit equals ecx (set for class 17), it sets bit 1 (2, jump pending), writes byte 10 to the high word (bytes 14-15) of xmmword_141862440, and returns byte 10.
- V: when the bit is clear, it sets bit 2 (4, continue) and returns the table dword that was read.

## Notes

The body at 0x1402F217C is shared with class 18, which enters with ecx 0. The table is read as dwords (byte 9 >> 5 selects the dword), so 256 bits span eight dwords. Class 21 sets bits and class 22 clears bits in the same table. The IDA name of this handler is still EventCmd_JumpIfByteFlagSet; no rename was made.

## Open questions

What the flags mean; which other code writes the table (sub_140218F78, sub_14021B0E8 and sub_14033FB84 reference it). Overlap: bits 64 to 255 here are ids 0 to 191 of dword_1411A7030 used by classes 15 and 16.
