# ClassicItemUi_OpAdvanceOpening

- **Address:** `0x14039D1EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpAdvanceOpening(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 22 of the item page script: advances the opening stage.

## Behavior

- V: as UiScript_OpAdvanceOpening (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the one-byte record returns record + 1.

## Open questions

None recorded.
