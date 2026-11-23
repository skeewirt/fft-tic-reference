# ClassicItemUi_OpSetDrawMode

- **Address:** `0x14039BD28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpSetDrawMode(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 24 of the item page script: a draw-mode change.

## Behavior

- V: as UiScript_OpSetDrawMode (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the queue entry is built inline with the value (32 * (+2 and 3)) | 4 and a mode command byte, at the item page's priority word.

## Open questions

None recorded.
