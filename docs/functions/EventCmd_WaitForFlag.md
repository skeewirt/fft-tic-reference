# EventCmd_WaitForFlag

- **Address:** `0x1402F28F8`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int16_t EventCmd_WaitForFlag(void)`
- **Callers:** EventCmd_Run through the class table, class 43
- **Callees:** sub_1400FC598 (returns 0 when the byte at qword_143CD9E60 + 20 + (byte at qword_143CD9E60 + 23) is 2. With its fourth argument 0 and second argument 32: when its first argument is non-zero it calls sub_1400F6C8C with the third argument and returns 1 when a masked result is non-zero. Then it reads the table at qword_143CD9EE8 + 1386 + 48 * 26 and returns 1 when the byte at either of the two 16-byte-spaced entries is non-zero, otherwise 0.)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 43 handler. Yields on every pass and continues only when a flag test passes: a table test in the no-object path, or the object's bit 0x80 otherwise.

## Behavior

- V: class 43 argument layout: bytes 9, 10 and 11 are not read. The test uses fixed constants (32, 26 and 0).
- V: sets bit 3 (value 8, yield) of the status word on every path.
- V: when the offset-48 dword of the object at qword_143CD9E28 is zero: sets bit 2 (value 4, continue) when sub_1400FC598 with dword_140D4CC18, 32, 26 and 0 returns non-zero; otherwise leaves bit 2 clear.
- V: when that dword is non-zero and bit 0x80 of the object's offset-64 dword is clear: sets bit 0x40 (value 64) of that dword and leaves bit 2 clear.
- V: when that dword is non-zero and bit 0x80 of the object's offset-64 dword is set: sets bit 2 (value 4, continue).
- V: writes the resulting status word back to the command register.

## Notes

The yield-and-continue shape reads as a wait-until-condition handler: it stays on the same command (yield) until the test passes. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What the table at qword_143CD9EE8 + 1386 + 48 * 26 holds and what entry index 26 means. What reads the bit 0x40 request flag at offset 64 of the object, and what sets bit 0x80. The meaning of dword_140D4CC18 and of the masked result in sub_1400FC598 (the decompiler hides the register).
