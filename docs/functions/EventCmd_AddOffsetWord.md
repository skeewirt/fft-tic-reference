# EventCmd_AddOffsetWord

- **Address:** `0x1402F2320`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_AddOffsetWord(void)`
- **Callers:** EventCmd_Run through the class table, class 26
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 26 event command: adds a 16-bit argument to the word at offset 2 of the global xmmword_141862450.

## Behavior

- V: class_note: argument bytes 9 (low byte) and 10 (high byte) form the 16-bit addend. Byte 11 is ignored by the addition; it appears only in the return value.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word.
- V: adds the addend to WORD1(xmmword_141862450), the word at offset 2 of that global, with the result truncated to 16 bits.
- V: returns the full 24-bit argument (bytes 9 to 11).
- V: calls no function and does not wait.

## Notes

Class 27 subtracts the same kind of argument from the same word; class 30 reads that word and resets it to zero.

## Open questions

What the word at offset 2 of xmmword_141862450 means to the game.
