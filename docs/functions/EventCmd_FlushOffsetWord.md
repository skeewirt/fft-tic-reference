# EventCmd_FlushOffsetWord

- **Address:** `0x1402F245C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_FlushOffsetWord(void)`
- **Callers:** EventCmd_Run through the class table, class 30
- **Callees:** sub_1401E02E8 (presence flag set)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 30 event command: adds the word at offset 2 of xmmword_141862450 to the high dword of qword_141862470, clamps the sum to 0 to 65535, resets that word to zero, and passes the result to sub_1401E02E8 when the state object is present.

## Behavior

- V: class_note: no argument bytes are read.
- V: forms the signed sum of the signed word at offset 2 of xmmword_141862450 and the signed high dword of qword_141862470.
- V: sets the word at offset 2 of xmmword_141862450 to 0.
- V: clamps the sum: a sum above 65535 becomes 65535; a negative sum becomes 0. The clamped value is written as the high dword of qword_141862470 and to dword_140D40A98; a negative sum writes 0 to dword_140D40A98.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word.
- V: when the presence flag (dword at +48 of qword_143CD9E28) is non-zero, calls sub_1401E02E8 with the state object and the clamped value, and returns its result. Otherwise returns the clamped value.
- V: does not wait.

## Notes

Reads the word that classes 26 and 27 change, and the high dword that classes 25 and 28 use.

## Open questions

What the clamped value means to sub_1401E02E8 and to the game; what dword_140D40A98 is used for.
