# EventCmd_RandomJump

- **Address:** `0x1402F2070`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `__int64 EventCmd_RandomJump(void)`
- **Callers:** EventCmd_Run through the class table, class 14
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 14: picks one of three command bytes at random and sets it as a pending jump value.

## Behavior

- V: argument layout: byte 9 is candidate 0, byte 10 is candidate 1, byte 11 is candidate 2; all three are read.
- V: advances the generator state in the four dwords of xmmword_1408E5FC8 inline: t = s0 xor (s0 shifted left 11); the dwords move down one place; the new top dword is s3 xor ((t xor (s3 shifted right 11)) shifted right 8) xor t, where s3 is the old top dword.
- V: the selector is (3 * (the low 15 bits of the new top dword, the word at bytes 12-13 of the state)) shifted right 15, giving 0, 1 or 2.
- V: the result is the candidate byte for the selector: byte 9 for 0, byte 10 for 1, byte 11 for 2.
- V: sets bit 1 (2, jump pending) of the status word and writes the result to the high word (bytes 14-15) of xmmword_141862440. Bit 2 is not set.
- V: returns the result.

## Notes

The generator is inline, not a called routine. The candidate is stored as a jump value; how the dispatcher reads the high word after a jump-pending result was not traced. The IDA name is still EventCmd_RandomJump; no rename was made.

## Open questions

Where the generator state is seeded; how the interpreter reads the high word after a jump-pending result.
