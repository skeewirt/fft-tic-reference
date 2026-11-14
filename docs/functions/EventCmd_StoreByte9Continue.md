# EventCmd_StoreByte9Continue

- **Address:** `0x1402F256C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_StoreByte9Continue(void)`
- **Callers:** EventCmd_Run through the class table, class 33
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 33: stores argument byte 9 in the word at offset 12 of xmmword_141862460 and sets the continue bit.

## Behavior

- V: argument layout: only byte 9 is read; bytes 10 and 11 are not read.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word.
- V: writes byte 9, zero-extended to 16 bits, to the word at offset 12 of xmmword_141862460 (a different global from the command register).
- V: returns byte 9; calls nothing and does not wait.

## Notes

Classes 28 and 32 also use xmmword_141862460 (word at offset 8, bytes at 10 and 11); nothing in this handler reads its offset 12 word back.

## Open questions

What the second command register (xmmword_141862460) is used for; nothing in this handler reads the stored value back.
