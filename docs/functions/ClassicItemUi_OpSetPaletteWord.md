# ClassicItemUi_OpSetPaletteWord

- **Address:** `0x14039BBD0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpSetPaletteWord(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 9 of the item page script: the palette word.

## Behavior

- V: as UiScript_OpSetPaletteWord (same record layout and result), over the draw globals of the item pages; the differences are listed below.

## Open questions

None recorded.
