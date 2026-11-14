# EventCmd_SetIdPrefixed

- **Address:** `0x1402F29EC`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetIdPrefixed(void)`
- **Callers:** EventCmd_Run through the class table, class 47
- **Callees:** sub_1402B20C0, sub_1402B2098 (stores the id in dword_141856AA8, calls sub_1402BA8E8 with it, and passes the result to sub_1401D80A8 on qword_143CD9DD8 with 12)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 47 handler: calls the reset helper, then passes byte 9 plus 0x10000 to sub_1402B2098.

## Behavior

- V: argument layout: byte 9 is the id; byte 10 is a flag; byte 11 is not read.
- V: when byte 10 is non-zero, the 16-bit word at 0x141862472 is set to byte 9 OR 0x4000; when byte 10 is zero, the word is not changed.
- V: calls sub_1402B20C0.
- V: calls sub_1402B2098 with byte 9 + 0x10000.
- V: sets bit 2 (value 4) of the status word (continue). Returns the value of sub_1402B2098.

## State touched

- Calls: [sub_1401D80A8](sub_1401D80A8.md)

## Notes

The 0x10000 added to the id is read from the code; its meaning is not known.

## Open questions

What the 0x10000 base means; what sub_1402BA8E8 and sub_1401D80A8 do with the id; the meaning of the 0x4000 bit in the word at 0x141862472.
