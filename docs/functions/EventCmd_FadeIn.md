# EventCmd_FadeIn

- **Address:** `0x1402F2784`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void EventCmd_FadeIn(void)`
- **Callers:** EventCmd_Run through the class table, class 41
- **Callees:** sub_1401E03AC (like sub_1401E0350 but calls sub_1401809F8: with byte 9 non-zero plays the FadeIn state of the GUI node at the rate 60 / byte 9, stops FadeOut, and sets bit 0x200 of the object's dword at offset 64; with 0 calls sub_1401809F8 with 0.0, which stops FadeOut and ends FadeIn at once.) sub_1402CCCD0 (see class 40).

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 41 handler. Starts a fade-in over byte 9 in 60ths of a second (instant when 0), clears bit 8 (0x100) of the status word, and continues.

## Behavior

- V: class 41 argument layout: only byte 9 is read; it is the duration in 60ths of a second. Bytes 10 and 11 are not read.
- V: sets bit 1 (value 2) of the state dword xmmword_140D8DC40.
- V: clears bit 8 (value 0x100) of the status word.
- V: when the dword at offset 48 of the object at qword_143CD9E28 is non-zero, calls sub_1401E03AC with the object and byte 9; otherwise calls sub_1402CCCD0 with 0 and byte 9.
- V: sets bit 2 (value 4, continue) in the status word.

## Notes

On the path without the object, bit 1 is set before the call and the argument 0 has it clear, so sub_1402CCCD0 sees a difference and rewrites the state to 1; bit 1 does not survive. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

Same open items as EventCmd_FadeOut. Why the bit 0x100 of the status word is cleared here and set by class 42.
