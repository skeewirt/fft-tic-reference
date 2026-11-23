# ClassicItemUi_OpScrollList

- **Address:** `0x14039C784`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpScrollList(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** sub_14039C554, sub_14039D2F0, sub_14039D204, Input_TestAction, Input_ActionBit, sub_140395FBC, GfxPacket_QueueRect, sub_1403953D8, sub_14039C388

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 16 of the item page script: a scrolling list.

## Behavior

- V: as UiScript_OpScrollList (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: the body reads +2 (cursor flag), +7, +8, +11, +12, +13 directly (+4 on the no-rows skip path, which skips like UiScript_OpScrollList); the row template count, row height and visible rows come from item page words. I: those words are filled by the pre-scan sub_14039C554, which was not read.
- V: the row template runs once per visible row (one more while the scroll offset is non-zero) with the list flag word set, as in UiScript_OpScrollList.
- V: unlike UiScript_OpScrollList the selection clamps at both ends (last row at the bottom, row 0 at the top) instead of wrapping.
- V: the thumb y is +12 + 15 plus the selected row times (+13 - +12 - 20) over (rows - 1), the same expression as in UiScript_OpScrollList.
- V: the key-repeat counter is its own word and advances by 2 per step (the scroll offset also moves by twice the table step); input starts with sub_14039D2F0 (called with 48, 0 and 256), whose result 0, 2 or other is handled as in the 29-slot version.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [GfxPacket_QueueRect](GfxPacket_QueueRect.md)

## Open questions

None recorded.
