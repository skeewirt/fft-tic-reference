# EventCmd_SetParamBlock

- **Address:** `0x1402F26C4`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetParamBlock(void)`
- **Callers:** EventCmd_Run through the class table, class 38
- **Callees:** sub_1402B1FB4 (writes the block at xmmword_140D3A910: dword 0 = 0xFFFFFC1C (-996), dword 1 = 0, dword 2 = 100 times the first argument divided by 127, dword 3 = the second argument. When qword_1418623A8 is non-zero it also stores the first argument in dword_1418623B8 and returns 1; otherwise returns 0.)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 38 handler. Clears bit 0 of the high dword of qword_140D49558, loads the parameter block at xmmword_140D3A910 through sub_1402B1FB4 (first argument 0, second byte 9), clears the byte at 0x14186246A, and continues.

## Behavior

- V: class 38 argument layout: only byte 9 is read, as the second argument of sub_1402B1FB4. Bytes 10 and 11 are not read.
- V: clears bit 0 (value 1) of the high dword of qword_140D49558 (0x140D4955C).
- V: calls sub_1402B1FB4 with ecx = 0 and edx = byte 9; the return value (0 or 1) is the handler's return.
- V: sets bit 2 (value 4, continue), then stores the low byte of ecx into byte 10 of xmmword_141862460 (0x14186246A). The callee leaves ecx unchanged, and ecx was cleared to 0 before the call, so this stores 0.
- I: the stored 0 clears the low byte of the word at 0x14186246A that class 39 and class 49 test; the high byte there (0x14186246B) is the signed slot index and is not touched.

## Referenced by

- Observed behaviours: [MusicCommandWordHasEighteenOperandsAndSixOfThemOnlyWriteZeroOrTestNonzero](../behaviors/MusicCommandWordHasEighteenOperandsAndSixOfThemOnlyWriteZeroOrTestNonzero.md), [MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath](../behaviors/MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath.md)

## Notes

The first argument is 0 here, so dword 2 of the block is 0. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What the block at xmmword_140D3A910 and the record at qword_1418623A8 represent (a volume or a queued parameter). The meaning of bit 0 of 0x140D4955C.
