# BookProgress_ResetConfirmInput

- **Address:** `0x140372990`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t BookProgress_ResetConfirmInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 20)
- **Callees:** TimImage_Parse, ImageDissolve_Step, EventTask_Start, sub_140371CAC, sub_140372C10

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Two-row question about the record of a book (table index 20): one answer clears the book's progress record.

## Behavior

- V: while record dword 4 is nonzero it only steps an image dissolve (TimImage_Parse, ImageDissolve_Step).
- V: cancel pops, starts event task 14, prints text id 47176 and calls sub_140371CAC with record dword 8; confirm starts the close (sets mask 0x4 of the state dword).
- V: after the close, a second-row answer (dword 5 nonzero) writes -1 to six words, 0 to several fields and 48 to the dword at +0x0A (0x1411A7576) of the 56-byte record of the book numbered word_140D8DBA4 (fields from 0x1411A756C, 56 bytes apart; g_BookProgressWords is one word of it), then calls sub_140372C10.
- I: the name rests on that record being the book progress record; the question wording was not read.
- V: the Yes/No toggles by record dword 5 and the cursor moves 16 pixels.

## State touched

- Calls: [TimImage_Parse](TimImage_Parse.md), [ImageDissolve_Step](ImageDissolve_Step.md), [EventTask_Start](EventTask_Start.md)

## Open questions

None recorded.
