# EventCmd_ClearMode

- **Address:** `0x1402F241C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_ClearMode(void)`
- **Callers:** EventCmd_Run through the class table, class 29
- **Callees:** sub_1401E0210 (presence flag set)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 29 event command: resets the state object's mode through sub_1401E0210 when the state object is present, clears status bit 7 and sets the continue bit.

## Behavior

- V: class_note: no argument bytes are read.
- V: when the presence flag (dword at +48 of qword_143CD9E28) is non-zero, calls sub_1401E0210 with the state object. Otherwise sets bit 0x800 (bit 11) of dword_141D32E14 (class 28 clears that bit in its absent path).
- V: sets WORD6(xmmword_141862440) to (its old value AND 0xFF7F) OR 4. That clears bit 7 (0x80) and sets bit 2 (continue); every other bit is kept.
- V: the return value is the updated status word.

## Notes

The counterpart of class 28, which sets bit 7.

## Open questions

The meaning of status bit 7 (0x80) and of dword_141D32E14 bit 0x800.
