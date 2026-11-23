# ClassicItemUi_OpSetPageWord

- **Address:** `0x14039BC98`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpSetPageWord(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 12 of the item page script: the texture-page attribute word.

## Behavior

- V: as UiScript_OpSetPageWord (same record layout and result), over the draw globals of the item pages; the differences are listed below.

## Open questions

None recorded.
