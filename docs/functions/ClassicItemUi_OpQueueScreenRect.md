# ClassicItemUi_OpQueueScreenRect

- **Address:** `0x14039D1B0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpQueueScreenRect(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** sub_140395734

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 21 of the item page script: the fixed screen rectangle.

## Behavior

- V: as UiScript_OpQueueScreenRect (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: through sub_140395734.

## Open questions

None recorded.
