# ClassicUi_OpScrollList

- **Address:** `0x1403911B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpScrollList(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript (through the 22-slot handler table)
- **Callees:** sub_1403910B0, sub_140391C90, sub_140391BA4, Input_TestAction, Input_ActionBit, sub_14038FD44, sub_14025FCDC, sub_140390FD8, sub_14038F560, sub_14038F3FC, sub_140390DE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 16 of the layout script table: the scrolling list.

## Behavior

- I: the same record fields as UiScript_OpScrollList (+2 cursor flag, +4 records per row, +5 row height, +6 visible rows, +7 / +8 origin, +11 cursor offset, +12 / +13 mark y) and the same row template loop; read by comparing the structure of the two bodies.
- I: same role as UiScript_OpScrollList; its input handling differs (a one-row-at-a-time move with a sentinel result of the repeat helper, 999) and its helpers are the layout script's own (sub_1403910B0, sub_140391C90, sub_140391BA4, sub_14038FD44, sub_140390FD8, sub_14038F560, sub_14038F3FC, sub_140390DE0).
- ?: the details of the input handling were not read line by line.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md)

## Notes

Opcode 16, the longest handler of the table.

## Open questions

?: input handling and scroll copy details.
