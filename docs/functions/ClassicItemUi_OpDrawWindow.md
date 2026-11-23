# ClassicItemUi_OpDrawWindow

- **Address:** `0x14039B2C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpDrawWindow(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table), ClassicItemUi_OpDrawWindowOpening
- **Callees:** sub_1403953D8, ClassicItemUi_OpFillTiles

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 0 of the item page script: a bordered window and its fill.

## Behavior

- V: as UiScript_OpDrawWindow (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: there is no style-2 case: the rectangle always comes from +3..+6; cells are queued without a tint and with the constant 4 as the page argument (sixth argument) of sub_1403953D8; the fill is ClassicItemUi_OpFillTiles on a scratch record.
- V: stores the style in byte +2 of the scratch record it hands to ClassicItemUi_OpFillTiles, and the sum of x and the packed width byte (+5) in an item page word that ClassicItemUi_OpScrollList uses as the x of its up and down marks.

## State touched

- Calls: [ClassicItemUi_OpFillTiles](ClassicItemUi_OpFillTiles.md)

## Referenced by

- Called by: [ClassicItemUi_OpDrawWindowOpening](ClassicItemUi_OpDrawWindowOpening.md)

## Open questions

None recorded.
