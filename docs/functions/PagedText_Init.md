# PagedText_Init

- **Address:** `0x14037A168`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall PagedText_Init(__int64 info)`
- **Callers:** EventViewer_EntryPage, sub_1403460C8, sub_14036D66C, sub_14036F25C, sub_140371CAC, sub_140374484, sub_140376040, sub_1403769CC, Errand_FinishDayPage
- **Callees:** WorldMenu_AllocOverlayRecord, WorldMenu_AllocWindowRecord, EventText_FindMessage, sub_1402D8E08, PagedText_DrawPage

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up a paged message window: reserves four sprite records and one window record, positions them from the info block, measures the message and draws its first page.

## Behavior

- V: `info` is a block of 32-bit fields; reserved indexes are stored back into it: four sprite records (`WorldMenu_AllocOverlayRecord`, each given a kind value in its record: 8, 9, 10 and 15) at info+56, +60, +64 and +72, and one window record (`WorldMenu_AllocWindowRecord`) at info+68.
- V: the first sprite record gets 0x810 ORed into its first dword (bits 4 and 11), the other three get a value held in a register; each also gets a zero dword and the value at info+76 as a parameter; the window record gets bit 8 (0x100, set with a bit instruction), info+76 and the qword at info+8.
- V: the sprites are placed with x derived from the width at info+16 and the origin at info+8, and y from info+12 plus 16 times the line count at info+20.
- V: looks the message up with `EventText_FindMessage(info+52)`, measures it with `sub_1402D8E08` (width into info+24, line count into info+28), zeroes info+84 and info+48, and sets info+80 to the line index of the last page: `(lines - 1) - (lines - 1) % info+20`.
- V: ends with `PagedText_DrawPage(info, 0)` and returns its result.
- I: the four sprite records are page-flip and scroll indicators (rests on `PagedText_Step`, which shows and hides them by bit 0x10).

## State touched

- Calls: [WorldMenu_AllocOverlayRecord](WorldMenu_AllocOverlayRecord.md), [WorldMenu_AllocWindowRecord](WorldMenu_AllocWindowRecord.md), [EventText_FindMessage](EventText_FindMessage.md), [PagedText_DrawPage](PagedText_DrawPage.md)

## Referenced by

- Called by: [Errand_FinishDayPage](Errand_FinishDayPage.md)

## Notes

V: whole body read. The name is ours. Field offsets are into the info block passed by the caller, not into a global.

## Open questions

?: the kinds 8, 9, 10 and 15 of the sprite records and the info fields at +36, +42, +46, +92, +100 and +104.
