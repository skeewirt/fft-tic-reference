# EventCmd_ClearBitArrayA

- **Address:** `0x1402F225C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_ClearBitArrayA(void)`
- **Callers:** EventCmd_Run through the class table, class 22
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 22 event command: clears one bit in the 256-bit array at qword_1411A7028, selected by argument byte 9, and sets the continue bit of the status word.

## Behavior

- V: class_note: argument byte 9 is read. Its low five bits are the bit number and its value shifted right by five (0 to 7) is the dword index into the array. Bytes 10 and 11 are not read.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word.
- V: clears the bit numbered (byte 9 AND 31) in the dword at index (byte 9 shifted right by 5) counted from the start of qword_1411A7028.
- V: calls no function and does not wait; no other status bit is changed.
- V: the return value is the complement of the single-bit mask that was cleared.

## Notes

Class 22 clears a bit in qword_1411A7028; class 23 sets and class 24 clears a bit in the separate array dword_140D4CC28.

## Open questions

What the array at qword_1411A7028 holds and what its bit numbers name; the size of the array is not shown by the decompiled code.
