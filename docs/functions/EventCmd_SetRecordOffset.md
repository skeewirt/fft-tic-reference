# EventCmd_SetRecordOffset

- **Address:** `0x1402F1DB0`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetRecordOffset(void)`
- **Callers:** EventCmd_Run through the class table, class 10
- **Callees:** sub_1403436C0, sub_140343564, sub_140340AE0, sub_140260718, sub_14025FF20, sub_140379D34

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 10 handler: loads three argument bytes into the command registers and, in mode zero, writes two offsets into a 14-dword record selected by a word of xmmword_141862450.

## Behavior

- V: stores argument byte 9 in the word at bytes 14-15 of xmmword_141862450, byte 11 in the word at bytes 14-15 of xmmword_141862460, and byte 10 in the low word of qword_141862470 (all three in both modes).
- V: the mode dword at +48 of the record in qword_143CD9E28 selects the path.
- V: mode zero: calls sub_1403436C0 with byte 9. When byte 9 differs from dword_140D498E8, it waits with sub_140343564 (yield loop), sets dword_140D498E8 to byte 9, reads dword_140684CD0[byte 9] and dword_140684CD0[byte 9 + 1] as start and length (the difference), and loads that block with sub_1403434D0 into qword_140D6D8B0 (call arguments include the constant 766).
- V: mode zero: calls sub_140343564 again (yield loop while the busy dword is non-zero).
- V: mode zero: the record index is the signed word at bytes 12-13 of xmmword_141862450 (not set by this handler). In the 14-dword record at that index in dword_140D4B9B0 (stride 0x38 bytes), dword +6 (offset 0x18) gets byte 11 minus 128 and dword +7 (offset 0x1C) gets byte 10 minus 120.
- V: mode zero: calls sub_140340AE0 on qword_140D6D8B0 + 4 to fill a local descriptor, then sub_140260718 and sub_14025FF20 with fields of that descriptor, then sub_140379D34 with the record index and four descriptor words, and finally sets dword +4 (offset 0x10) of the record to 0.
- V: the handler sets bit 2 (0x4) in all cases.
- V: all three bytes 9, 10 and 11 are read.

## Notes

Byte 9 selects a data block (mode zero) and is kept in the second command register. Bytes 10 and 11 become offsets biased by -120 and -128 in the record. The record index comes from a word not set by this handler.

## Open questions

Where the word at bytes 12-13 of xmmword_141862450 is set; what the record fields in dword_140D4B9B0 are used for; what sub_1403434D0, sub_140260718, sub_14025FF20 and sub_140379D34 do (not read); what the descriptor from sub_140340AE0 holds.
