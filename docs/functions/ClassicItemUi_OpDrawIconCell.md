# ClassicItemUi_OpDrawIconCell

- **Address:** `0x14039B210`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpDrawIconCell(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** the row callback, sub_14039B050

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 6 of the item page script: a picture cell from a row callback's descriptor.

## Behavior

- V: as UiScript_OpDrawIconCell (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the descriptor bytes and words are copied into a scratch cell record and its palette and page words, then the item page's draw-cell handler (sub_14039B050, slots 4 and 5) runs on the scratch record. I: the field order follows UiScript_OpDrawIconCell.

## Open questions

None recorded.
