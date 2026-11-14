# EventCmd_WaitIfBusy

- **Address:** `0x1402F1BD0`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void* EventCmd_WaitIfBusy(void)`
- **Callers:** EventCmd_Run through the class table, class 4
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 4 handler: sets either the continue bit or the wait bit depending on a state test.

## Behavior

- V: reads the mode dword at +48 of the record in qword_143CD9E28.
- V: mode zero: tests the qword at index 3602 of off_14078D5D8 (byte offset 28816). When it is zero, the test passes.
- V: mode non-zero: tests the byte at +64 of the record in qword_143CD9E28 against 0x18 (bits 3 and 4). When the masked value is zero, the test passes.
- V: when the test passes, sets bit 2 (0x4); otherwise sets bit 3 (0x8).
- V: the handler returns the record pointer (mode non-zero) or off_14078D5D8 (mode zero).
- V: class 4 reads no argument byte (bytes 9, 10 and 11 are not used).

## Notes

The bit tests are the only conditions; no write to the record occurs.

## Open questions

What the qword at off_14078D5D8 index 3602 and the bits 3 and 4 of the byte at +64 represent.
