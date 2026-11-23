# UiScript_OpScrollList

- **Address:** `0x140329548`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpScrollList(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** sub_1403293E8, sub_140329310, sub_14032A0F0, sub_14032A004, Input_TestAction, Input_ActionBit, sub_140303EC8, sub_14031EA20, Prim_QueueKind6Record, sub_14025FCDC, sub_14031DA24, sub_140328F0C, the handlers of the template records

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 16: draws a scrolling list: repeats the records that follow once per visible row, reads the up and down input, animates the scroll and draws the marks, thumb and cursor.

## Behavior

- V: record: +2 draw-cursor flag, +4 records per row template, +5 row height in pixels, +6 visible rows, +7 and +8 list origin, +11 cursor x offset, +12 and +13 y of the up and down marks; +9 and +10 are two bytes whose product divided by 4 is kept in a shared word used by the scroll copies.
- V: a pre-scan helper (sub_1403293E8, run while a state byte is set) walks the records until opcode 16 or opcode 30 (?: opcode 30 has no slot in the 29-slot table) or the end opcode 33; at the list record it copies +4, +5, +6 into the row template, row height and visible row words and clamps the selected row and the first visible row to the row count.
- V: the row count is the number of ids in the row table given to the script; with no rows the handler skips this record and the following +4 template records (a conditional record counts with its governed records) and returns.
- V: sets the list flag word to 1 while rows are drawn (records inside read the row from the row counter), runs the template records once per visible row (one more while the scroll offset is non-zero) and clears the flag afterwards. The row counter restarts at 0.
- V: input: action 0x21 selects the previous row and action 0x22 the next one (unless a repeat helper, sub_14032A0F0, reports otherwise). At the window edge the list scrolls by animating a pixel offset in steps taken from a small table (a first step size for the first frames, another after) until a full row has passed, then the first visible row advances. Selecting past an end wraps to the other end.
- V: when the alternate-value flag is clear (a byte that the state reset sub_140329E1C sets from the third argument of UiScript_Run) it draws an up mark, a down mark and a thumb positioned by the selected row over the row count; with the cursor flag set it draws the animated pointing cursor beside the selected row (sub_140328F0C).
- V: returns the pointer after the last template record run (just after this record when no row was drawn).
- V: the row table is an array of 16-bit ids ended by 0xFFFF (sub_140327854 counts to the terminator when the script is set up; sub_140329310 writes one when it rebuilds the visible ids). I: the scroll copies move the drawn rows as a block through helpers that were not read (sub_14031EA20, Prim_QueueKind6Record, sub_14025FCDC).
- ?: the meaning of the +9 and +10 pair and of the helper sub_14032A004.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [Prim_QueueKind6Record](Prim_QueueKind6Record.md)

## Notes

Helpers read: sub_1403293E8, sub_140329310, sub_140327854, sub_14032A0F0 and sub_140328F0C; the scroll copy helpers are not read.

## Open questions

?: the timing tables (scroll step sizes, key repeat).
