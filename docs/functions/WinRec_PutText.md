# WinRec_PutText

- **Address:** `0x140379C68`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall WinRec_PutText(int rec, int textRef, __int64 point, int buffer)`
- **Callers:** PagedText_DrawPage, sub_1402D4C60, sub_1402F1690, sub_140318A1C (four calls), sub_14036A294 (four calls), EventVarEditor_DrawPage, sub_140371550 (four calls), sub_140374B50, sub_140377118, sub_140379CCC, __ld12mul_2 (three calls)
- **Callees:** sub_1402EC9D0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a message into a window record: hands the text reference, a target buffer and a point plus a record width to `sub_1402EC9D0`.

## Behavior

- V: `rec` indexes the window record array at 0x140D4B9B0 (14 dwords, 0x38 bytes each; records are handed out in order by WorldMenu_AllocWindowRecord, which also pushes the record's address on the allocation stack at qword_140D4C0B0).
- V: builds a local block {point.x (u16), point.y (u16), the signed 16-bit value at address 0x140D4B9DC + 56 * rec (record byte 0x2C, reached as a displaced address, so the array base 0x140D4B9B0 does not appear as an operand)} and calls `sub_1402EC9D0(textRef, buffer, &block)`, returning its result.
- I: `sub_1402EC9D0` is the menu-side text command thunk (documented); the third value may be the line width the text is wrapped at (rests on the field's position next to the record's rectangle; not verified).

## State touched

- Calls: [sub_1402EC9D0](sub_1402EC9D0.md)

## Referenced by

- Called by: [EventVarEditor_DrawPage](EventVarEditor_DrawPage.md), [PagedText_DrawPage](PagedText_DrawPage.md), [sub_14036A294](sub_14036A294.md), [sub_140371550](sub_140371550.md)

## Notes

V: whole body read. The name is ours.

## Open questions

I: the field at record byte 0x2C is the rectangle's width word: `WinRec_SetRect` stores the packed rectangle there, `WinRec_SetSource` stores twice the descriptor's third word, and `WinRec_CopyToVram` divides it by 4.
