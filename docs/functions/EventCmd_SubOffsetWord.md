# EventCmd_SubOffsetWord

- **Address:** `0x1402F233C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SubOffsetWord(void)`
- **Callers:** EventCmd_Run through the class table, class 27
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 27 event command: subtracts a 16-bit argument from the word at offset 2 of the global xmmword_141862450.

## Behavior

- V: class_note: argument bytes 9 (low byte) and 10 (high byte) form the 16-bit subtrahend. Byte 11 is ignored by the subtraction; it appears only in the return value.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word.
- V: subtracts the subtrahend from WORD1(xmmword_141862450), with the result truncated to 16 bits.
- V: returns the full 24-bit argument (bytes 9 to 11).
- V: calls no function and does not wait.

## Notes

The mirror of class 26, on the same word.

## Open questions

What the word at offset 2 of xmmword_141862450 means to the game.
