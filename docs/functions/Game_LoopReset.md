# Game_LoopReset

- **Address:** `0x140283FCC`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall Game_LoopReset(__int64 unused)`
- **Callers:** Game_MainLoopReset (0x1402D4A30)
- **Callees:** sub_140273D78, sub_14025F7C0, sub_1402B1CD0, EventThread_Yield, sub_140283E24, sub_1402B2124, sub_140283F64

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The one-time reset before the outer loop: it sets the 374x240 screen mode, clears the fade, battle and event state, resets the event counters, calls the scene/UI reset helpers, and seeds the constant block.

## Behavior

- V: calls `sub_140273D78` with 374 and 240.
- V: clears the state word `dword_142FF9EFC` that the hand-over path and the battle routines read, plus `dword_142FF9F04`, `g_ScreenFadeMode` and the low dword of `xmmword_142FF9E14`.
- V: zeroes 0x80 bytes at `byte_1418622F0` and the four event counters at 0x141856700, 0x141856704, 0x141856708 and 0x141856928.
- V: calls `sub_14025F7C0` and `sub_1402B1CD0`, clears the high dword of `qword_141856AB0`, yields one event tick, clears it again, then calls `sub_140283E24`, `sub_1402B2124` and `sub_140283F64`.
- V: clears the scene-UI initialized flag `dword_141856718` and `unk_142E7FAFC`, and writes a two-qword constant block to `xmmword_1408E5FC8`.
- ?: what the seeded constant block and the three reset helpers control.

## State touched

- Calls: [EventThread_Yield](EventThread_Yield.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md)
- Called by: [Game_MainLoopReset](Game_MainLoopReset.md)

## Notes

Whole function read (201 bytes). This is the reset body; the 15-byte wrapper `Game_MainLoopReset` calls it and then enters `Game_MainLoop`.

## Open questions

The identity and full effect of the event and screen helpers called here.
