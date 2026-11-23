# ClassicItemUi_OpFillTiles

- **Address:** `0x14039B914`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpFillTiles(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table), ClassicItemUi_OpDrawWindow
- **Callees:** sub_1403953D8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 17 of the item page script: a rectangle filled with 16-pixel tiles.

## Behavior

- V: as UiScript_OpFillTiles (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the cells go through sub_1403953D8 without a tint and with the constant 4 as the page argument of sub_1403953D8; the style-2 rectangle comes from item page words.
- ?: who fills the style-2 rectangle words of the item page (ClassicItemUi_OpDrawWindow does not write them).

## Referenced by

- Called by: [ClassicItemUi_OpDrawWindow](ClassicItemUi_OpDrawWindow.md)

## Open questions

None recorded.
