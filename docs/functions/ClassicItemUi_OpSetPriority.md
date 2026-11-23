# ClassicItemUi_OpSetPriority

- **Address:** `0x14039BE14`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpSetPriority(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 15 of the item page script: the priority word.

## Behavior

- V: as UiScript_OpSetPriority (same record layout and result), over the draw globals of the item pages; the differences are listed below.

## Open questions

None recorded.
