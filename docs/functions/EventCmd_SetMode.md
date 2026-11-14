# EventCmd_SetMode

- **Address:** `0x1402F2358`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetMode(void)`
- **Callers:** EventCmd_Run through the class table, class 28
- **Callees:** sub_1401E0068 (presence flag set), sub_1401E02E8 (presence flag set, byte 9 not 2)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 28 event command: records a mode byte, then, when the state object is present, drives the state object through sub_1401E0068 and sub_1401E02E8; when it is absent, it sets several global words instead. It sets the continue bit and bit 7 of the status word.

## Behavior

- V: class_note: argument byte 9 is the mode (0 to 255). Bytes 10 and 11 are not read.
- V: stores byte 9 in the word at offset 8 of xmmword_141862460 (word 4 of that global).
- V: when the presence flag (dword at +48 of qword_143CD9E28) is non-zero: byte 9 equal to 2 calls sub_1401E0068 with mode 3 only. Byte 9 equal to 3 calls sub_1401E02E8 with the state object and the signed high dword of qword_141862470, then sub_1401E0068 with mode 2. Every other byte 9 value (0, 1 and the rest) calls sub_1401E02E8 with the same arguments, then sub_1401E0068 with mode 1.
- V: when the presence flag is zero: clears bit 0x800 of dword_141D32E14; stores byte 9 in dword_140D49420; sets dword_140D40A98 to the high dword of qword_141862470 unless byte 9 is 2, in which case it is left unchanged; sets the low dword of qword_140D4CA08 to -32 and the high dword to 84; sets dword_140D49398 to 10.
- V: in both paths sets bit 2 (value 4, continue) and bit 7 (value 0x80) of WORD6(xmmword_141862440), the status word. The return value is 132 (0x84).
- V: does not wait.

## Notes

sub_1401E0068 changes the state object's mode dword (+424) only when that mode is currently 0, and then stores the requested value. Class 29 clears bit 7 again.

## Open questions

The meaning of status bit 7 (0x80); the meaning of dword_141D32E14 bit 0x800, dword_140D49420, qword_140D4CA08, dword_140D49398 and dword_140D40A98; what the mode values 1, 2 and 3 select in sub_1401E0068.
