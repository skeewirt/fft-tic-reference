# UiScript_OpIf

- **Address:** `0x140327954`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpIf(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** the row callback, the handlers of the governed records

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 1: runs the next records only while a row callback accepts the current row, otherwise skips them.

## Behavior

- V: record: +1 length, +3 callback index into the row callback table (g_ShopRowCallbacks), +4 count of governed records, +5 immediate argument.
- V: the argument is the list row: in list mode (a flag word that is set while a scrolling list draws its rows) it is the row counter plus the first visible row, minus 1 while the scroll offset is negative; otherwise it is the immediate operand.
- V: when the callback returns non-zero the governed records are run one by one through the 29-slot handler table (each returns the next record); otherwise each is skipped by its own length byte, one step of one record length per governed record, headers included. ?: whether scripts nest conditional records (a nested one would step over its header only). Contrast: the no-rows skip of UiScript_OpScrollList adds the governed counts of conditional records.
- V: returns the pointer after the governed records.

## Notes

Same shape as ClassicUi_OpIf of the 22-slot table, with a callback index instead of a page condition table.

## Open questions

None recorded.
