# UiScript_OpDrawIconCell

- **Address:** `0x140327CF4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpDrawIconCell(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** the row callback, sub_140327B7C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 6: draws one picture cell whose source rectangle comes from a row callback.

## Behavior

- V: record: +2 callback index, +3 immediate argument (replaced by the list row in list mode), +4 and +5 x and y.
- V: the callback returns a pointer to a descriptor (or 0, which draws nothing): bytes at +0, +2, +4, +6 become the cell's source x, source y, width and height, the word at +8 the palette word and the word at +10 the page word.
- V: it fills a scratch cell record (position from +4, +5) and runs the draw-cell handler of slots 4 and 5 (sub_140327B7C, which reads the scratch record as +3 x, +4 y, +5 and +6 size, +7 and +8 source x and y, applies the list row offset to y and queues the cell). I: so the descriptor bytes are the source x and y and the size, in that order of use. Returns the pointer after this record.

## Notes

Item-page twin: ClassicItemUi_OpDrawIconCell.

## Open questions

?: the first two bytes of the scratch record (static data that the draw-cell handler tests).
