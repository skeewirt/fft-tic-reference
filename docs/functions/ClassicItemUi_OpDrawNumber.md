# ClassicItemUi_OpDrawNumber

- **Address:** `0x14039BE28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpDrawNumber(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** sub_14032A204, sub_1403953D8, the row callback

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 13 of the item page script: a number or a gauge from a row callback.

## Behavior

- V: as UiScript_OpDrawNumber (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: only slot 13 exists here: leading positions always draw a zero glyph (sizes 0 and 1); no tint is passed.
- V: the third size (other than 0 and 1) does draw digits here, from two texture rows (digits 0..7 and 8..9) with its own palette word.
- V: gauge cells sit one pixel further left than in UiScript_OpDrawNumber.

## Open questions

None recorded.
