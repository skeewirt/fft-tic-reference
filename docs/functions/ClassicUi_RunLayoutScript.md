# ClassicUi_RunLayoutScript

- **Address:** `0x14038FFB8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ClassicUi_RunLayoutScript(const unsigned char *script)`
- **Callers:** sub_14039297C (job screen task), ClassicJobDetailPage_Run and one more call site outside any function
- **Callees:** the opcode handlers ClassicUi_Op*

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one layout script of the legacy menus: a list of records that draw windows, cells and numbers.

## Behavior

- V: resets the draw state (the priority word, the layer word and the plate flag) and remembers the current input id, then walks the records.
- V: each record is {opcode, record length, arguments}; the handler of the opcode comes from a 22-slot function table (0x140693110; opcodes 3, 6, 7, 8 and 11 have no handler, 4 and 5 share one) and returns the start of the next record (this record + its length byte).
- V: stops at opcode 22; afterwards a global page redraw counter is incremented while it is below 10.

## Referenced by

- Called by: [ClassicJobDetailPage_Run](ClassicJobDetailPage_Run.md)

## Notes

Read: the loop and the table; the handlers named below are the ones read. A second runner of the same kind (25 opcodes, end opcode 25, table 0x1406932A0) is inlined in the item pages.

## Open questions

?: the handler of opcode 16 (a long one) and the small handlers of opcodes 19..21.
