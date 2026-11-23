# ClassicItemUi_OpDrawLine

- **Address:** `0x14039B110`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpDrawLine(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 7 of the item page script: a line between two points.

## Behavior

- V: as UiScript_OpDrawLine (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the entry is filled inline: end points (+2, +3) and (+4, +5), both x values plus 128, the colour from +6..+8.

## Open questions

None recorded.
