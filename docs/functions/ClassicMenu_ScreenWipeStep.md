# ClassicMenu_ScreenWipeStep

- **Address:** `0x1402CC42C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ClassicMenu_ScreenWipeStep(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 35; also sub_14014DC80)
- **Callees:** sub_14015D8DC, sub_14014EA60, sub_1402CC130, sub_14025FE14, sub_1400F5828

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a screen wipe (table index 35): a frame-counted fade and slide of the picture layers, with a phase in the record.

## Behavior

- V: record dword 0 is the frame counter (incremented at the end of every pass); dword 3 the phase (0, 1 or 2) of the slide that moves two layer words by one pixel per frame; dword 4 the fade phase (1 raises three colour bytes at 0x140D8DC64 by 16 until 0x80, 2 raises them by 8 until 0xF8).
- V: when the fade reaches full it toggles mask 0x1 of the state dword, sets 0x142FF9E14 to 1 and starts the follow-up window (sub_14014EA60 on the window object).
- V: in phase 0, when dword 5 equals 2, it plays cue 0x90 if dword 8 is 0 and cue 0xDD otherwise; with dword 8 nonzero and dword 5 equal to 56 it sets mask 0x8 of the fade control dword 0x140D8DC40.
- V: while the map window reports state 1 it only steps that window (sub_14015D8DC) and calls sub_1402CC130.

## Notes

Read at the level of its phases; the layer arithmetic was not decoded.

## Open questions

? which two layers slide and what scene starts the wipe.
