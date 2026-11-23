# PagedText_DrawPage

- **Address:** `0x14037A940`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall PagedText_DrawPage(__int64 info, int firstLine)`
- **Callers:** PagedText_Init, PagedText_Step, sub_14037A694 (three calls); also a data reference at 0x143D3F2EC
- **Callees:** WinRec_SetRect, WinRec_PutText, WinRec_CopyToVram

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one page of a paged message window starting at a given line: rebuilds the window rectangle, positions the extra marker, draws the text and copies the window to the video page.

## Behavior

- V: stores `firstLine` in `dword_14184B2B4` and `firstLine + info[5]` in `dword_14078DBD4`.
- V: builds the rectangle (info x u16 at +0, y u16 at +4, width `(u16 at +16 + 24) & 0xFFFC`, height `16 * (info[5] + 1)`) and calls `WinRec_SetRect(info[17], rect, info[23], dword_140D858C0)`.
- V: when `g_LanguageInfo` is null or its dword at +8 is non-zero, it copies two dwords from info+104 into `xmmword_14078D9C0` (skipping values of -1) and, when info+100 is not -1, positions or hides (bit 0x10) that window record by the line offset `info[9] - 16 * firstLine`.
- V: draws the text with `WinRec_PutText(info[17], info[13], point (8, 8), dword_140D858C0)` (the pseudocode shows the point as one 64-bit constant, 8 in each half), copies it with `WinRec_CopyToVram(info[17])` and stores the qword at info+8 in the record's dwords 6..7. Returns that qword.

## State touched

- Calls: [WinRec_SetRect](WinRec_SetRect.md), [WinRec_PutText](WinRec_PutText.md), [WinRec_CopyToVram](WinRec_CopyToVram.md)

## Referenced by

- Called by: [PagedText_Init](PagedText_Init.md), [PagedText_Step](PagedText_Step.md)

## Notes

V: whole body read. The name is ours. `info[17]` is the window record index (info+68), `info[13]` the text reference (info+52).

## Open questions

?: what the optional record at info+100 is and the use of `dword_14184B2B4` and `dword_14078DBD4`.
