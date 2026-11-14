# EventMapTitle_DrawSweep

- **Address:** `0x140302318`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventMapTitle_DrawSweep(void *buffer, int value, int unused, int layout)`
- **Callers:** EventMapTitle_SweepTask (three call sites: 0x1403029F4, 0x140302A7C and 0x140302AFA).
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds four 184-byte map-title draw records for one sweep value into a 736-byte buffer and links them into the draw list; the layout argument (0 or 1) chooses the record variant and the link order.

## Behavior

- V: reads the running task block (slot dword_140D40948). The dword at +0 is the X base and the dword at +8 is the Y base. The 0x91 handler stored operand 1 and operand 2 there, so these are the two operand bytes.
- V: the third argument is not read. The sweep task always passes 100.
- V: the four records are at buffer + 0, + 184, + 368 and + 552. The record index is twice the row (0 or 1) plus the column (0 or 1).
- V: all four records get these fixed fields: dword -1 at +76 and at +80, +84, +88, +92, +96, +100, +104, +108, +112, +116 and +120; word 42 at +10; byte 62 at +15; word 16348 at +22; qword 0 at +60; qword 255 at +68; word 0 at +172; byte 0 at +174; dword 0 at +176; word 39 at +34 for column 1 and 71 for column 0.
- V: row 0 (the first two records) sets the colour bytes to 100 at +12 to +14, +24 to +26, +36 to +38 and +48 to +50.
- V: row 1 with layout 0 sets 100 at +12 to +14 and +36 to +38, and 0 at +24 to +26 and +48 to +50. With layout 1 it is the reverse: 100 at +24 to +26 and +48 to +50, and 0 at +12 to +14 and +36 to +38.
- V: the value and the X and Y bases give the position words (+16, +18, +28, +30, +40, +42, +52, +54) and the value bytes (+20, +32, +44, +56); the glyph word of the language (next line) is added to some of them. Clamps apply for values of 32 and up and 223 and up. The full arithmetic is not restated here.
- V: the glyph word is word_1408EB93E when g_LanguageInfo is non-null and its dword at +8 is zero, and word_1408EBA2E otherwise (including when g_LanguageInfo is null).
- V: when the float at dword_142C81554 is 2.0 or more, the dword at +60 of each of the four records is set to 11111.
- V: linking, layout 0: the list head is the qword that qword_140D40868 points to. The records are pushed in the order record 3, record 2, record 1, record 0, so the list reads head, record 0, record 1, record 2, record 3, then the old list. Layout 1 gives head, record 2, record 3, record 0, record 1, then the old list. Each record's word at +8 is set to word_14114A4E4.
- V: calls nothing else.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [EventMapTitle_SweepTask](EventMapTitle_SweepTask.md)

## Notes

The buffer is one of two alternating 736-byte areas at unk_1437A5400. The sweep task passes layout 1 only in its third phase.

## Open questions

What reads the draw list at qword_140D40868 and what each record field (+10, +15, +20, +21, +22, +32, +33, +34, +44, +45, +56, +57, +60, +68, +172, +174, +176) means on screen; the exact arithmetic of the position words.
