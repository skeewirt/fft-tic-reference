# EventCmd_JumpIfFlagClear

- **Address:** `0x1402F2168`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_JumpIfFlagClear(void)`
- **Callers:** EventCmd_Run through the class table, class 16
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 16: jumps to the byte 11 target when the bit for the 16-bit id in bytes 9 and 10 is clear in the flag table at dword_1411A7030.

## Behavior

- V: argument layout: bytes 9 (high) and 10 (low) form the 16-bit id; byte 11 is the jump value. All three are read.
- V: the entry is a two-instruction stub: it sets ecx to 0 (xor ecx, ecx) and jumps to the body at 0x1402F210C, which is shared with class 15.
- V: id = byte 9 * 256 + byte 10; tests bit (id & 31) of dword_1411A7030[id >> 5], as in class 15.
- V: when the bit is clear, it sets bit 1 (2, jump pending), writes byte 11 to the high word (bytes 14-15) of xmmword_141862440, and returns byte 11.
- V: when the bit is set, it sets bit 2 (4, continue) and returns the table dword that was read.

## Notes

The decompiler shows only the stub at this address; the behavior was read from the disassembly of the shared body at 0x1402F210C. The IDA name is still EventCmd_JumpIfFlagClear; no rename was made.

## Open questions

Same as class 15, including the overlap of dword_1411A7030 with the table at qword_1411A7028 (id N is bit N+64 there).
