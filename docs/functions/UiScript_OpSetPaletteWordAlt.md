# UiScript_OpSetPaletteWordAlt

- **Address:** `0x140328780`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpSetPaletteWordAlt(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 10: as slot 9 with a second operand set for the alternate-value flag.

## Behavior

- V: the flag is the third argument of UiScript_Run (stored by the state reset): clear = operands +2..+4, set = operands +5..+7 (same packing as slot 9).
- V: returns the pointer after the record.

## Notes

Same role as ClassicUi_OpSetTexturePageB.

## Open questions

None recorded.
