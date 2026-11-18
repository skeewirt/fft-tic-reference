# BattleCommand_StoreCursorRow

- **Address:** `0x1402EB828`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char BattleCommand_StoreCursorRow(void)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Remembers the cursor row of the current battle command menu for the acting unit.

## Behavior

- V: scans the first 12 rows of the menu cursor default table (0x1408B9EE0) for the current menu number (dword_14078D518).
- V: on a match copies the byte at +80 of that menu node (88 bytes per node, node array = qword_14184B230) into the per-unit cursor memory (17 bytes per unit slot at 0x1408BA0D0).

## Referenced by

- Reads tables: [MenuCursorDefaults](../tables/MenuCursorDefaults.md)

## Notes

Read in full.

## Open questions

?: why only 12 of the 31 rows are scanned.
