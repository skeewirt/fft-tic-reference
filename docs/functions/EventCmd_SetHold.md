# EventCmd_SetHold

- **Address:** `0x1402F1F38`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_SetHold(void)`
- **Callers:** EventCmd_Run through the class table, class 12
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 12: sets or clears the hold state (bit 6 of the status word) and the matching bits on the current scene records. Argument byte 9 is the switch.

## Behavior

- V: argument layout: byte 9 is the switch (nonzero sets, zero clears); bytes 10 and 11 are not read.
- V: when byte 9 is nonzero it sets bit 6 (0x40) of the status word. If the dword at offset 48 of the object at qword_143CD9E28 is nonzero it sets bit 12 (0x1000) of the dword at offset 64 of that object. Otherwise it computes index = 23 * (dword_140D8DBA0 - 1) (stride 0x5C bytes) and clears bit 4 (0x10) of dword_140D4C4B0[9 * e] for e = dword_140D8D8C0[index] and e = dword_140D8D8C4[index].
- V: when byte 9 is zero it clears bit 6 of the status word; with an active object it clears bit 12 (0x1000) of the dword at offset 64, otherwise it sets bit 4 (0x10) on the same two dword_140D4C4B0 records (record stride 9 dwords).
- V: in both cases it then sets bit 2 (4, continue) of the status word.
- V: the return value is dword_140D8D8C4[index] in the no-object case, otherwise the object pointer qword_143CD9E28.
- I: the 23-entry index stride and the 9-dword record stride are read from the index arithmetic; the record layouts are not named.

## Notes

Each index selects a pair of records that are updated together. The handler is inline and calls nothing. The IDA name is still EventCmd_SetHold; no rename was made.

## Open questions

What the bit 6 (0x40) hold state means to readers of the status word; what dword_140D8DBA0 counts; what the records addressed through dword_140D8D8C0 and dword_140D8D8C4 are.
