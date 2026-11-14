# EventCmd_FadeOut

- **Address:** `0x1402F273C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void EventCmd_FadeOut(void)`
- **Callers:** EventCmd_Run through the class table, class 40
- **Callees:** sub_1401E0350 (reads the GUI node at ((qword_143CD9DA8 + 16) + 248) + 64. When byte 9 is non-zero: calls sub_140180B50 with byte 9 over 60 seconds when the node exists, and sets bit 0x200 of the object's dword at offset 64. When zero: calls sub_140180B50 with 0.0, which stops FadeIn and ends FadeOut at once.) sub_1402CCCD0 (when bit 1 of the state differs from bit 1 of its first argument: sets bit 3 of dword_141D32E14, clears dword 0 of xmmword_140D8DC50, stores its second argument in dword 1, sets the state to the first argument OR 1, and for bits 0x20 and 0x10 of the argument calls sub_14033FDAC.)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 40 handler. Starts a fade-out over byte 9 in 60ths of a second (instant when 0) and continues.

## Behavior

- V: class 40 argument layout: only byte 9 is read; it is the duration in 60ths of a second. Bytes 10 and 11 are not read.
- V: the state dword xmmword_140D8DC40 is replaced by (state AND 0xFFFFFFFD) OR 8: bit 1 (value 2) is cleared and bit 3 (value 8) is set.
- V: when the dword at offset 48 of the object at qword_143CD9E28 is non-zero, calls sub_1401E0350 with the object and byte 9.
- V: when that dword is zero, calls sub_1402CCCD0 with 2 and byte 9.
- V: sets bit 2 (value 4, continue) in the status word.

## Notes

On the path without the object, bit 1 is cleared first, so sub_1402CCCD0 sees a difference and sets the state to 3. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What the object at qword_143CD9E28 is, and what the dword at its offset 48 and the state at xmmword_140D8DC40 mean to the game. The fade-out target node is reached through qword_143CD9DA8 and offsets 16, 248 and 64.
