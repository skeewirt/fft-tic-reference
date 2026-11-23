# MenuCtl_Entry50

- **Address:** `0x1402D18D0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t MenuCtl_Entry50(void)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 50)
- **Callees:** sub_140248A50, sub_140248A98, WorldMenu_RunTopOpenHook

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Short step of a controller that closes itself once its window is done (table index 50).

## Behavior

- V: when sub_140157BBC() is nonzero and the window object reports no pending state (field at +2464 of its first window is 0, or the window is absent) it calls sub_140248A50 with the entry of the 52-byte table at 0x140D4AFD8 picked by the record's first dword; with sub_140157BBC() zero it goes straight on.
- V: when mask 0x1 of the dword 0x140D4B968 is set it calls sub_140248A98, sets mask 0x1 of qword_140D493E0 and the redraw mask 0x2 of the state dword.
- V: otherwise it clears mask 0x2000, pops, copies the pair (x, y - 4) from the 52-byte table at 0x140D4AFF8 (the entry picked by this record's first dword) into the cursor entry of the screen below, and calls WorldMenu_RunTopOpenHook.

## State touched

- Calls: [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Open questions

? which screen pushes it.
