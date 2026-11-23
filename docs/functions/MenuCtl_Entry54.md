# MenuCtl_Entry54

- **Address:** `0x1402D1DA8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry54(unsigned int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 54)
- **Callees:** sub_1401DF558, sub_140340FD0, sub_1401585A8, sub_14015845C, WorldMenu_RunTopOpenHook

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a one-shot window controller (table index 54): a state dword starts a window action, then it pops.

## Behavior

- V: record dword 3 nonzero starts it, but only after mask 0x8 of the state dword is clear and, when sub_140157BBC() is nonzero, sub_1401585A8 succeeds; with dword 1 nonzero it plays cue 2, otherwise it calls sub_1401DF558(dword 0, 1) and plays cue 0x77; then dword 3 is cleared.
- V: dword 2 is a frame counter: nonzero it keeps the redraw mask set and counts down (with the window present it is cleared by sub_14015845C being 0 instead).
- V: when it is 0 the pop path runs: with dword 1 set it sets mask 0x10 in the 52-byte table at 0x140D4AFE0 (entry of dword 0), calls sub_1401DF558(dword 0, 0) and, with the window present, sub_140340FD0; it then clears mask 0x10 of the screen below's entry in 0x140D4C4B0, sets the redraw mask and calls WorldMenu_RunTopOpenHook.

## State touched

- Calls: [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Open questions

? the screen that uses it.
