# ClassicItemUi_OpQueueScreenRectOnce

- **Address:** `0x14039D0FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpQueueScreenRectOnce(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** sub_140395734

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 19 of the item page script: the fixed screen rectangle after a window animation.

## Behavior

- V: as UiScript_OpQueueScreenRectOnce (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the rectangle primitive goes through sub_140395734.

## Open questions

None recorded.
