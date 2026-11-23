# ClassicMenu_PopTownMenu

- **Address:** `0x140345EFC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ClassicMenu_PopTownMenu(int *record)`
- **Callers:** sub_1403456D4, sub_1403465B4
- **Callees:** sub_1400EDCB4, WorldMenu_RunTopOpenHook

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Pops a menu screen and lowers the window counters for the windows it opened.

## Behavior

- V: record dwords 1 to 4 name windows; each one that is not -1 lowers two of the counters 0x140D4CA00, 0x140D4C974 and 0x140D4C978, and every window lowers 0x140D4C978.
- V: it clears 0x140D498D0 and lowers the stack depth; then, depending on the result of the window-present test sub_140157BBC(), it calls sub_1400EDCB4 and, under a further condition, re-opens the screen below with WorldMenu_RunTopOpenHook; it finally clears mask 0x2000 of the state dword.
- I: it is the exit of the town menu, from its callers sub_1403456D4 and sub_1403465B4.

## State touched

- Calls: [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Open questions

None recorded.
