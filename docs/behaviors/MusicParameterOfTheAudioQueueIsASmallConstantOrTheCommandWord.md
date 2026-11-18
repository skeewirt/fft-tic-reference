# MusicParameterOfTheAudioQueueIsASmallConstantOrTheCommandWord

- **Kind:** observed behaviour
- **Scope:** engine (audio command queue, kind 1)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [sub_14034004C](../functions/sub_14034004C.md), [sub_14033FDAC](../functions/sub_14033FDAC.md), [sub_14033FE00](../functions/sub_14033FE00.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every stock producer of a kind 1 (play music) entry of the audio command queue passes either a small constant or the 16-bit command word of the command state; no stock parameter has a bit above 0x2FF set, so bits 12 and up of the parameter are free.

## Behavior

- V: the push function sub_14033FDAC takes (kind, parameter); a kind 1 entry is pushed by exactly two bodies: sub_14034004C (its own argument, after an optional kind 2 entry and before a kind 3 entry) and, as plain constants, two direct pushes (parameter 0x11B in sub_14033F8C0, 0x221 in the function at 0x140370E14).
- V: the direct calls of sub_14034004C load ecx with 0x11B (four calls), 0x220 (two calls in the function at 0x1403793DC, one of which is also reached with 0x21A), 0x221 (two), 0x223 (one), or the sign-extended 16-bit command word (sub_1402F109C at 0x1402F1298); no call passes a computed value.
- V: the worker sub_14033FE00 decodes a kind 1 parameter at 0x14033FFC3..0x14033FFCF: the slot is bits 8..11, the music id is the low byte (movzx of dil), and everything above bit 11 is ignored.
- I: the command word of a stock game only holds values below 0x300 (the id is a byte and the slot byte is 0 or 2), so a stock parameter is below 0x300 on every route.

## Notes

Indirect calls (through a function pointer) were not searched: none of the direct pushers is a table entry, and the queue is private to the audio command functions.

## Open questions

? a push through a function pointer (none found).
