# UiScript_OpFillRect

- **Address:** `0x140327AF0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpFillRect(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** sub_14031D768

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 3: queues a flat-coloured rectangle.

## Behavior

- V: record: +2 x, +3 y, +4 and +5 two extents (I: width and height), +6..+8 the colour bytes. In list mode y gets the row offset: the scroll offset plus the row counter times the row height, minus one row height while the scroll offset is negative.
- V: passes the rectangle, the colour, the blend flag word and the priority word to sub_14031D768 (the flat rectangle queue, which adds 128 to x) and returns the pointer after the record.

## Notes

Item-page twin: ClassicItemUi_OpFillRect, which fills the queue entry inline.

## Open questions

None recorded.
