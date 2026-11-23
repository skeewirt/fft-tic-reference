# ClassicItemUi_OpFillRect

- **Address:** `0x14039AF2C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpFillRect(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 3 of the item page script: a flat-coloured rectangle.

## Behavior

- V: as UiScript_OpFillRect (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the queue entry is filled inline (x + 128, y, the two extents, the colour from +6..+8, the blend word and the item page's priority word) instead of through a helper; the y gets the list row offset in list mode.

## Open questions

None recorded.
