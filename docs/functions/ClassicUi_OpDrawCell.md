# ClassicUi_OpDrawCell

- **Address:** `0x1403901D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpDrawCell(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** sub_14038F3FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcodes 4 and 5: queues one sprite cell.

## Behavior

- V: arguments are the cell x (+3), y (+4, shifted by the list row when a list page is drawn), texture position (+5, +6) and the cell size (+7, +8); opcode 4 uses no shared rectangle word, opcode 5 passes the shared one.
- V: passes the current layer, blend and texture page words to the cell queue.

## Open questions

None recorded.
