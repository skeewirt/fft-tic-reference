# EventCmd_ReleaseSlot

- **Address:** `0x1402F2A90`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_ReleaseSlot(void)`
- **Callers:** EventCmd_Run through the class table, class 49
- **Callees:** sub_1402B1ED0, sub_1402B1E74 (clears the slot arrays at qword_1418623C0, qword_1418623F8 and dword_142E7FB08 when the slot is in use)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 49 handler: when the 16-bit word at 0x14186246A is non-zero, releases the slot whose signed index is the byte at 0x14186246B and clears its entry.

## Behavior

- V: argument layout: no command argument byte is read; the handler works from the state block at 0x141862460 (the word at 0x14186246A and the signed byte at 0x14186246B).
- V: when the word at 0x14186246A is non-zero: clears bit 0 of the dword at 0x140D4955C, calls sub_1402B1ED0, calls sub_1402B1E74 with the slot index, sets the word at 0x14186246A to 0, sets the dword at qword_140D49560 + 4*index to 0 and sets dword_140D49568 to 0.
- V: when the word is zero, none of these steps run.
- V: sets bit 2 (value 4) of the status word (continue).

## Notes

Return value: the slot index when the word is non-zero, otherwise whatever the return register held on entry. The word at 0x14186246A and the signed byte at 0x14186246B overlap (the byte is the high byte of the word). Class 38 writes 0 to the low byte; class 53 does not write these bytes.

## Open questions

What the slot arrays and dword_142E7FB24 represent; the meaning of the word at 0x14186246A; why the zero path returns the entry register.
