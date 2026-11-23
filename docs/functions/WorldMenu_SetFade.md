# WorldMenu_SetFade

- **Address:** `0x1402CD714`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall WorldMenu_SetFade(unsigned int fadeId, unsigned char mode)`
- **Callers:** EventViewer_EntryPage, JournalPanel_Tick, Tavern_TopInput, sub_14014DC80, sub_1402B4038, sub_1402B425C, sub_1402B4710
- **Callees:** UIState_BeginTransition, sub_1402CCCD0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Requests a UI fade state and then sets the world-menu mode word.

## Behavior

- V: when `fadeId` differs from the requested state at `g_UIStateFade+24`, it zeroes the fade timer at +16 if the old state was non-zero, stores the new state and calls `UIState_BeginTransition` on `g_UIStateFade+16`.
- V: it then jumps to `sub_1402CCCD0` with arguments `16*mode + 2` and 1; that helper does nothing unless bit 1 of its first argument differs from `xmmword_140D8DC40`, in which case it sets bit 3 of `dword_141D32E14`, stores the value or 1 and the second argument, and for bits 0x20 and 0x10 queues four audio commands through `sub_14033FDAC`.
- V: returns the helper's result.

## Notes

Both functions read.

## Open questions

What the mode word's high nibble selects.
