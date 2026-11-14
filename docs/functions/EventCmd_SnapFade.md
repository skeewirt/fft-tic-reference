# EventCmd_SnapFade

- **Address:** `0x1402F27CC`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SnapFade(void)`
- **Callers:** EventCmd_Run through the class table, class 42
- **Callees:** sub_1401809F8 (with 0.0: stops FadeOut and ends the FadeIn state of the GUI node at once). sub_140180B50 (with 0.0: stops FadeIn and ends the FadeOut state at once).

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 42 handler. Byte 9 non-zero snaps the screen to the faded-in state, byte 9 zero snaps it to the faded-out state; both set the yield and continue bits.

## Behavior

- V: class 42 argument layout: only byte 9 is tested (zero or non-zero). Bytes 10 and 11 are not read.
- V: when byte 9 is non-zero: clears bit 2 (value 4) of dword_1437FC2C0 when the object's dword at offset 48 is zero; clears bit 3 (value 8) of dword_141D32E14; sets the state dword to (state AND 0xFFFFFFF4), which clears bits 0, 1 and 3.
- V: in that non-zero path, when the object's offset-48 dword is zero: clears bit 8 (0x100) of the status word, clears the 16-bit field at offset 4 and the byte at offset 6 of xmmword_140D8DC60, and sets dword_140789370, dword_140789368 and dword_14078936C to 128.
- V: in that non-zero path, when the offset-48 dword is non-zero: calls sub_1401809F8 with 0.0 on the GUI node when the node exists.
- V: when byte 9 is zero: clears bit 3 (value 8) of dword_141D32E14; sets the state dword to (state AND 0xFFFFFFF4) OR 8, which clears bits 0 and 1 and sets bit 3.
- V: in that zero path, when the offset-48 dword is non-zero: calls sub_140180B50 with 0.0 on the GUI node when the node exists.
- V: in that zero path, when the offset-48 dword is zero: sets the 16-bit field at offset 4 and the byte at offset 6 of xmmword_140D8DC60 to 0xFFFF and 0xFF, sets bit 8 (0x100) of the status word, and sets dword_140789370, dword_140789368 and dword_14078936C to 0.
- V: in both branches the final status word has bits 2 and 3 set (value 0xC) and is written back to the command register.

## Notes

Name is inferred from the 0.0 calls; the handler returns the final status word. Both branches set bit 3 (yield) and bit 2 (continue). Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What the fields at xmmword_140D8DC60 and the globals dword_140789368, dword_140789370, dword_14078936C and dword_1437FC2C0 hold. What dword_141D32E14 bit 3 means. The 0x100 status bit is set and cleared in this handler; its meaning is not established.
