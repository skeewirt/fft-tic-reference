# ClassicItemUi_OpSetPaletteWordAlt

- **Address:** `0x14039BC1C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpSetPaletteWordAlt(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 10 of the item page script: the palette word with an alternate operand set.

## Behavior

- V: as UiScript_OpSetPaletteWordAlt (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the alternate-value flag is a byte of the item page; the packing is the one of slot 9.

## Open questions

None recorded.
