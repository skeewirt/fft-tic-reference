# EventCmd_SetScreenRgb

- **Address:** `0x1402F2AE8`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetScreenRgb(void)`
- **Callers:** EventCmd_Run through the class table, class 50
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 50 handler: when the dword at offset 48 of qword_143CD9E28 is zero, stores bytes 9, 10 and 11 into three dwords, which class 42 sets to 128 or 0 as a group; continues.

## Behavior

- V: argument layout: byte 9 goes to dword_140789370, byte 10 to dword_140789368 and byte 11 to dword_14078936C; the three bytes are read only when the test passes.
- V: reads the dword at offset 48 of qword_143CD9E28; when it is zero the three stores run.
- V: sets bit 2 (value 4) of the status word (continue) in every case.
- V: returns byte 11 when the stores ran, otherwise the pointer qword_143CD9E28.

## Notes

Name is inferred: the three dwords are the ones class 42 resets to neutral 128 or to 0, which reads as three color channels. The return value differs on the two paths; the caller does not use it.

## Open questions

What qword_143CD9E28 is and what the dword at offset 48 means; what the three destination dwords are used for.
