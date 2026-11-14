# EventCmd_Yield

- **Address:** `0x1402F1F00`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_Yield(void)`
- **Callers:** EventCmd_Run through the class table, class 11
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 11 handler: marks the current record (bit 4 of its first dword, mode zero only), sets the continue and wait bits in the status word, and sets the high word of the second command register to -1.

## Behavior

- V: argument layout: bytes 9, 10 and 11 are not read by this handler.
- V: when the dword at offset 48 of the object at qword_143CD9E28 is 0, it sets bit 4 (0x10) of dword_140D4B9B0[14 * w], where w is the signed word at bytes 12-13 of xmmword_141862450 (the second command register).
- V: sets bits 2 and 3 (0xC, continue and yield) of the status word at bytes 12-13 of xmmword_141862440.
- V: sets the word at bytes 14-15 of xmmword_141862450 to -1.
- V: returns -1 (0xFFFFFFFF).

## Notes

The index w comes from the second command register, not from the command bytes. The IDA name of this handler is still EventCmd_Yield; no rename was made.

## Open questions

What the record at dword_140D4B9B0 is and what the 0x10 bit means to the scheduler; what reads the high word of the second command register.
