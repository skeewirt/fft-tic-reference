# ClassicItemUi_OpQueueRect

- **Address:** `0x14039D14C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpQueueRect(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** sub_140395734

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 20 of the item page script: a rectangle from the record.

## Behavior

- V: as UiScript_OpQueueRect (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: through sub_140395734.

## Open questions

None recorded.
