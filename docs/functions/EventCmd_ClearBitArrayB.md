# EventCmd_ClearBitArrayB

- **Address:** `0x1402F22B8`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_ClearBitArrayB(void)`
- **Callers:** EventCmd_Run through the class table, class 24
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 24 event command: clears one bit in the 256-bit array at dword_140D4CC28, selected by argument byte 9, and sets the continue bit of the status word.

## Behavior

- V: class_note: argument byte 9 is read. Its low five bits are the bit number and its value shifted right by five (0 to 7) is the dword index into the array. Bytes 10 and 11 are not read.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word.
- V: clears the bit numbered (byte 9 AND 31) in the dword at index (byte 9 shifted right by 5) of dword_140D4CC28.
- V: calls no function and does not wait; no other status bit is changed.
- V: the return value is the complement of the single-bit mask that was cleared.

## Notes

Paired with class 23, which sets a bit in the same array. Class 22 clears a bit in qword_1411A7028, a different array.

## Open questions

What the array dword_140D4CC28 holds and what its bit numbers name; the size of the array is not shown by the decompiled code.
