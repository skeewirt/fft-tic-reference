# HelpMessage_Wait

- **Address:** `0x14036DA40`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void *HelpMessage_Wait(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 3)
- **Callees:** WorldMenu_RunTopOpenHook

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the help message screen (table index 3): waits until the message window has finished, then closes.

## Behavior

- V: when the screen two levels down is kind 28 or 37 it first copies three globals (0x141856700, 04, 08) into 0x140D4941C, 0x140D40A98 and 0x140D492C8.
- V: when the busy field of the message object at 0x14078D5D8 (offset 0x1090) is zero it pops, stores the record's second dword in 0x140D498D0, re-opens the screen below and, when the first dword is nonzero, restores the 128-byte block like PagedText_WaitAndClose.

## State touched

- Calls: [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Open questions

None recorded.
