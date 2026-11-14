# EventCmd_JumpIfFlagSet

- **Address:** `0x1402F2100`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_JumpIfFlagSet(void)`
- **Callers:** EventCmd_Run through the class table, class 15
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 15: jumps to the byte 11 target when the bit for the 16-bit id in bytes 9 and 10 is set in the flag table at dword_1411A7030.

## Behavior

- V: argument layout: bytes 9 (high) and 10 (low) form the 16-bit id; byte 11 is the jump value. All three are read.
- V: the entry sets ecx to 1 and jumps to the shared body at 0x1402F210C.
- V: id = byte 9 * 256 + byte 10; tests bit (id & 31) of dword_1411A7030[id >> 5]; the body compares that bit with ecx.
- V: when the bit equals ecx (set for class 15), it sets bit 1 (2, jump pending), writes byte 11 to the high word (bytes 14-15) of xmmword_141862440, and returns byte 11.
- V: when the bit is clear, it sets bit 2 (4, continue) of the status word and returns the table dword that was read.

## Notes

The body at 0x1402F210C is shared with class 16, which enters with ecx 0 so it jumps when the bit is clear. The decompiler shows only the part from this entry; the rest was read from the disassembly. EventCmd_Run itself sets bits in the same table (instruction at 0x1402F151E, a read-modify-write with the same byte 9 * 256 + byte 10 id). The IDA name of this handler is still EventCmd_JumpIfFlagSet; no rename was made.

## Open questions

Which other code writes dword_1411A7030 (EventCmd_Run does; several other functions reference it); what the returned table dword means when the bit is clear (the caller may ignore it). Overlap: dword_1411A7030 equals dword index 2 of the table at qword_1411A7028 used by classes 17, 18, 21 and 22, so id N here is bit N+64 there.
