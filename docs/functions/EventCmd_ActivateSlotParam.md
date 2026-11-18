# EventCmd_ActivateSlotParam

- **Address:** `0x1402F26F0`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_ActivateSlotParam(void)`
- **Callers:** EventCmd_Run through the class table, class 39
- **Callees:** sub_1402B1F08 (calls sub_1402B1ED0, which resets the block at xmmword_140D3A900 from xmmword_140723AE0 and clears the record at qword_1418623A8. When the slot index is 0 it returns 0. Otherwise it sets dword_142E7FB24 to index-1, loads the block at xmmword_140D3A900 from dword_142E7FB08[index] and the three dwords at dword_14067FBB0 + 12 * that value, and when qword_1418623F8[index] is non-zero stores the slot into dword_1418623A0, qword_1418623B0 and qword_1418623A8 and sets dword_1418623B8 to 0.) sub_1402B1FB4 (see class 38).

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 39 handler. When the word at 0x14186246A is non-zero, sets bit 0 of the flag dword at 0x140D4955C, activates the slot whose signed index is the byte at 0x14186246B through sub_1402B1F08, and loads the parameter block through sub_1402B1FB4 with byte 9; then continues.

## Behavior

- V: class 39 argument layout: only byte 9 is read, as the second argument of sub_1402B1FB4. Bytes 10 and 11 are not read from the command.
- V: tests the 16-bit word at 0x14186246A (offset 10 of xmmword_141862460). When it is zero, no call is made.
- V: when it is non-zero: sets bit 0 (value 1) of the high dword of qword_140D49558, calls sub_1402B1F08 with ecx = the signed byte at 0x14186246B, edx = 0 and r8 = 0, then calls sub_1402B1FB4 with dword_140D4956C as the first argument and byte 9 as the second, and returns that result.
- V: sets bit 2 (value 4, continue) in every case.
- V: the signed slot index at 0x14186246B is the high byte of the word tested at 0x14186246A (overlapping fields).

## Referenced by

- Observed behaviours: [MusicCommandWordHasEighteenOperandsAndSixOfThemOnlyWriteZeroOrTestNonzero](../behaviors/MusicCommandWordHasEighteenOperandsAndSixOfThemOnlyWriteZeroOrTestNonzero.md), [MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath](../behaviors/MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath.md)
- Reads tables: [MusicSlotRecords](../tables/MusicSlotRecords.md)

## Notes

The return value is not assigned when the word is zero. The decompiler hides the argument registers of sub_1402B1F08; the disassembly shows the slot index passed in ecx. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What the slot tables qword_1418623F8, qword_1418623C0 and dword_142E7FB08 hold, and the table at dword_14067FBB0. The meaning of dword_140D4956C. Who writes the slot index at 0x14186246B.
