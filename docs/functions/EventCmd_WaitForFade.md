# EventCmd_WaitForFade

- **Address:** `0x1402F2B6C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_WaitForFade(void)`
- **Callers:** EventCmd_Run through the class table, class 52
- **Callees:** sub_140180CA8 (returns 0 when the node's dword at offset 64 is 0; returns 1 when the FadeIn state or, failing that, the FadeOut state has its byte at offset 105 non-zero; releases up to two handles through sub_1403D8D1C)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 52 handler: yields the command loop while a fade is running on the GUI node or while a flag bit is set, and continues otherwise.

## Behavior

- V: class 52 argument layout: no command argument byte is read.
- V: when the dword at offset 48 of qword_143CD9E28 is non-zero: takes the node pointer at ((qword_143CD9DA8 + 16) + 248) + 64; when it is non-zero and sub_140180CA8 on it returns non-zero, the handler yields.
- V: in that branch, when the fade test does not yield (or the pointer is zero), the handler yields if bit 0x200 of the dword at offset 64 of qword_143CD9E28 is set, and continues if it is clear.
- V: when the dword at offset 48 is zero: yields if bit 3 (value 8) of dword_141D32E14 is set, and continues if it is clear.
- V: yield sets bit 3 (value 8) of the status word; continue sets bit 2 (value 4); only one of the two is set.

## Notes

Bit 0x200 is set by classes 40 and 41 when the duration is non-zero; bit 3 of dword_141D32E14 is set by sub_1402CCCD0 and cleared by class 42.

## Open questions

What qword_143CD9DA8, qword_143CD9E28 and dword_141D32E14 are, and when bit 0x200 is cleared. The handles released by sub_140180CA8.
