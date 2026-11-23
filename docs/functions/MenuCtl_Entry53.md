# MenuCtl_Entry53

- **Address:** `0x1402D1ABC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry53(int64_t record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 53)
- **Callees:** EventVar_Write, sub_1401585A8, sub_14015845C, WorldMenu_RunTopOpenHook

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a controller that walks through a chain of pages (table index 53), moving forward or backward with the record's direction.

## Behavior

- V: it keeps a page index (word 0x140D4B896), a page count (0x140D4B894) and an in-page counter (0x140D4B8B8) against a per-page length array at 0x140D4B898; a forward step increments the in-page counter and, past the page length, the page index.
- V: reaching the end writes event variable (word 0x140D4B892 + 556) = 1; stepping back past the start leaves the chain.
- V: when the chain is left it pops, clears mask 0x10 of the screen below's window entry, sets the redraw mask and calls WorldMenu_RunTopOpenHook.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Open questions

? which screens push it.
