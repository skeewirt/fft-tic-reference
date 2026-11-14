# EventCmd_JumpIfByteFlagClear

- **Address:** `0x1402F21C8`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_JumpIfByteFlagClear(void)`
- **Callers:** EventCmd_Run through the class table, class 18
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 18: jumps to the byte 10 target when the bit for byte 9 is clear in the flag table at qword_1411A7028 (a flag indexed by one byte).

## Behavior

- V: argument layout: byte 9 is the bit index (0 to 255); byte 10 is the jump value; byte 11 is not read.
- V: the entry is a two-instruction stub: it sets ecx to 0 and jumps to the body at 0x1402F217C shared with class 17.
- V: tests bit (byte 9 & 31) of the dword at qword_1411A7028 + 4 * (byte 9 >> 5), as in class 17.
- V: when the bit is clear, it sets bit 1 (2, jump pending), writes byte 10 to the high word (bytes 14-15) of xmmword_141862440, and returns byte 10.
- V: when the bit is set, it sets bit 2 (4, continue) and returns the table dword that was read.

## Notes

The decompiler shows only the stub; the behavior was read from the disassembly of the shared body. The IDA name is still EventCmd_JumpIfByteFlagClear; no rename was made.

## Open questions

Same as class 17.
