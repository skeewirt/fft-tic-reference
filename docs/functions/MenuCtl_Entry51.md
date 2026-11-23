# MenuCtl_Entry51

- **Address:** `0x1403462A4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t MenuCtl_Entry51(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 51)
- **Callees:** PagedText_Step, WorldMenu_RunTopOpenHook

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a screen that runs the paged text widget under a window with a pending close mask (table index 51).

## Behavior

- V: the global 0x140D495C4 holds a window index; when that window has mask 0x10 set the step waits for mask 0x8 of the state dword to clear (I: a fade), then plays cue 0x12 and clears 0x10 on that window and on the record's first window.
- V: otherwise, unless that window is busy (mask 0x100), it runs PagedText_Step on the widget block at 0x140D49580; when that returns 0 it lowers the window counters, clears masks 0x8000000 and 0x2000 of the state dword, pops and re-opens the screen below.

## State touched

- Calls: [PagedText_Step](PagedText_Step.md), [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Open questions

None recorded.
