# ClassicItemUi_OpSetTint

- **Address:** `0x14039BDD0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpSetTint(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 11 of the item page script: the tint colour.

## Behavior

- V: as UiScript_OpSetTint (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the alternate-value flag is the item page's byte; the colour is stored in the item page's tint record.

## Open questions

None recorded.
