# WinRec_SetRect

- **Address:** `0x140379AAC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall WinRec_SetRect(int rec, RECT16 rect, unsigned int page, __int64 extra)`
- **Callers:** PagedText_DrawPage, sub_1402D4C60, sub_140318A1C, sub_14036A294, EventVarEditor_DrawPage, sub_140371550, sub_140373BB0, sub_140374B50, sub_140377118, sub_140379CCC, __ld12mul_2
- **Callees:** WinRec_PageToVramPoint, sub_1402B4F0C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one window record from a rectangle and a texture page number, derives the page's packed texture word, and finishes through `sub_1402B4F0C` with the rectangle's width and height.

## Behavior

- V: `rec` indexes the window record array at 0x140D4B9B0 (14 dwords, 0x38 bytes each; records are handed out in order by WorldMenu_AllocWindowRecord, which also pushes the record's address on the allocation stack at qword_140D4C0B0); `rect` is four signed 16-bit values packed in a 64-bit argument (x, y, width, height).
- V: clears bits 2..4 of the record's first dword, zeroes dword 8, stores x - 128 in dword 6 and y - 120 in dword 7, stores the page in dword 3, stores 481 in dword 9 and the packed rectangle in dwords 10..11.
- V: calls `WinRec_PageToVramPoint(page, rect, &pt)`, then forms dword 1 as `((pt.x >> 6) & 0xF) | ((v >> 4) & 0x10) | (4 * (v & 0x200))` where v is `pt.y` when it is below 512 and `pt.y & 0x1FF` otherwise; dword 4 is zeroed; dword 12 gets 0x8080 (low word) and 0x80 (byte 2).
- V: ends with a tail jump to `sub_1402B4F0C(width, height, extra)` and returns its result.
- I: dword 1 is a packed texture-page word and the 0x8080 / 0x80 values are a neutral tint (rests on the bit layout: 4-bit column, a high-row bit and a 0x200 bit, as in a console GPU texture-page word).

## State touched

- Calls: [WinRec_PageToVramPoint](WinRec_PageToVramPoint.md)

## Referenced by

- Called by: [EventVarEditor_DrawPage](EventVarEditor_DrawPage.md), [PagedText_DrawPage](PagedText_DrawPage.md), [sub_14036A294](sub_14036A294.md), [sub_140371550](sub_140371550.md), [sub_140373BB0](sub_140373BB0.md)

## Notes

V: whole body read. The name is ours.

## Open questions

?: the role of the constant 481 in dword 9 and of `sub_1402B4F0C`.
