# EventCmd_Stop

- **Address:** `0x1402F1AD8`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void* EventCmd_Stop(void)`
- **Callers:** EventCmd_Run through the class table, class 0
- **Callees:** sub_1401DFF60 (mode non-zero path); sub_1400DF354 (through sub_1401DFF60, not read)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 0 handler: sets the stop bit in the status word and, depending on the mode flag, either marks the state of the script runner or passes the record to a helper.

## Behavior

- V: sets bit 5 (0x20) of the status word (the word at bytes 12-13 of xmmword_141862440) unconditionally.
- V: the mode dword at +48 of the record in qword_143CD9E28 selects the path.
- V: mode non-zero: the handler tail-jumps to sub_1401DFF60 with that record. sub_1401DFF60 sets bit 2 of the dword at +64 of the record, builds a local object whose vtable symbol is named vftable_ffto::Game::Achievement::NovelReadThroughNotification, stores the dword at +80 of the record in it, and calls sub_1400DF354 with qword_143CD9E30 and that object (the body of sub_1400DF354 was not read). The handler returns that call's result.
- V: mode zero: sets the qword at index 1042 of off_14078D5D8 (byte offset 8336) to 1, clears bit 11 (0x800) of dword_1437FC2C0, sets dword_143792300 to 1, and returns off_14078D5D8.
- V: class 0 reads no argument byte (bytes 9, 10 and 11 are not used).
- V: the handler does not set bit 1, 2 or 3 itself.

## Notes

The stop bit is the only status bit this handler sets for the caller.

## Open questions

What the stop bit does in EventCmd_Run and its caller (not traced); what off_14078D5D8 index 1042 and dword_1437FC2C0 bit 11 mean; what sub_1400DF354 does.
