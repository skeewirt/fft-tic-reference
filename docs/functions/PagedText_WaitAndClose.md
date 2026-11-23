# PagedText_WaitAndClose

- **Address:** `0x14036D870`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int *PagedText_WaitAndClose(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 2)
- **Callees:** PagedText_Step, WorldMenu_RunTopOpenHook

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a screen that only runs the paged text widget until it finishes (table index 2).

## Behavior

- V: runs the widget step PagedText_Step on the widget block at 0x140D49580 each frame; while it returns nonzero nothing else happens.
- V: when it returns 0 it lowers the window counters, pops the screen, stores the record's second dword in 0x140D498D0 and, when the first dword is nonzero, copies 128 bytes from 0x143789A50 back to 0x14184A8A0.
- V: it then calls WorldMenu_RunTopOpenHook to re-open the screen below.

## State touched

- Calls: [PagedText_Step](PagedText_Step.md), [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Notes

PagedText_Step was read in full: state 0 waits for confirm or cancel and pages forward by the page step, state 1 steps the page to the target, state 2 settles; I: a text pager.

## Open questions

? what the saved 128-byte block is.
