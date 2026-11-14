# EventCmd_SelectIndexedSet

- **Address:** `0x1402F295C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SelectIndexedSet(void)`
- **Callers:** EventCmd_Run through the class table, class 44
- **Callees:** sub_1402F1868 (calls sub_1402B20C0, sub_1402BA7C4 four times)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 44 handler: stores a 16-bit value in the event command word at 0x141862472 and selects an indexed set of four values through sub_1402F1868.

## Behavior

- V: argument layout: byte 9 is the set number n; byte 10 is a flag; byte 11 is not read.
- V: when byte 10 is non-zero, the 16-bit word at 0x141862472 is set to byte 9; when byte 10 is zero, that word keeps its previous value.
- V: calls sub_1402F1868 with byte 9 (the set number n).
- V: sub_1402F1868 calls sub_1402B20C0, then reads four bytes at byte_140681D00 + 4*(n-1), adds 14745600 to each and calls sub_1402BA7C4 with each value minus 1, in order.
- V: sets bit 2 (value 4) of the status word (continue).

## Notes

The table byte_140681D00 is indexed with 4*n-4, so n is a one-based set number; n = 0 would read before the table. The byte-9 value that is stored is the same value that is passed on.

## Open questions

What the four values passed to sub_1402BA7C4 mean; what the word at 0x141862472 is read for; sub_1402B20C0 and sub_1402BA7C4 not traced below one level.
