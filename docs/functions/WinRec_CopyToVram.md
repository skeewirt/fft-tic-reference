# WinRec_CopyToVram

- **Address:** `0x140379BE8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall WinRec_CopyToVram(int rec)`
- **Callers:** PagedText_DrawPage, sub_1402D4C60, sub_1402F1690, sub_140318A1C, sub_14036A294, EventVarEditor_DrawPage, sub_140371550, sub_140373DE8, sub_140374B50, sub_140377118, sub_140379CCC, __ld12mul_2
- **Callees:** WinRec_PageToVramPoint, VramPage_CopyRect

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a window record's rectangle into the video page, at the point its texture page maps to.

## Behavior

- V: `rec` indexes the window record array at 0x140D4B9B0 (14 dwords, 0x38 bytes each; records are handed out in order by WorldMenu_AllocWindowRecord, which also pushes the record's address on the allocation stack at qword_140D4C0B0).
- V: calls `WinRec_PageToVramPoint(dword 3, the packed rectangle in dwords 10..11, &pt)`, builds a rectangle (pt.x, pt.y, the record's word at dword 11 divided by 4, the record's word at dword 11 + 2 bytes) and calls `VramPage_CopyRect` with it.
- V: the second argument of `VramPage_CopyRect` is a register the pseudocode does not show being set; the function returns that call's result.

## State touched

- Calls: [WinRec_PageToVramPoint](WinRec_PageToVramPoint.md), [VramPage_CopyRect](VramPage_CopyRect.md)

## Referenced by

- Called by: [EventVarEditor_DrawPage](EventVarEditor_DrawPage.md), [PagedText_DrawPage](PagedText_DrawPage.md), [sub_14036A294](sub_14036A294.md), [sub_140371550](sub_140371550.md), [sub_140373DE8](sub_140373DE8.md)

## Notes

V: whole body read. The name is ours.

## Open questions

?: where the source pixel pointer for `VramPage_CopyRect` comes from (an unshown register).
