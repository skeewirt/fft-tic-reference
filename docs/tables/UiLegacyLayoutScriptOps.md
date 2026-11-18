# UiLegacyLayoutScriptOps

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140693110`
- **Rows:** 22 rows of 8 bytes
- **Keyed by:** layout script opcode 0..21
- **Row layout:** [CodePointerRow](../structs/CodePointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Handlers of the 22 opcodes of the legacy layout script (the record language of the job choice, job detail and other legacy pages: {opcode, length, arguments} until opcode 22). Verdict: code-table.

## Behavior

- V: slots with no handler are 3, 6, 7, 8 and 11; opcodes 4 and 5 both draw a cell
- V: named handlers: window frame (0), if (1), if-else (2), draw cell (4, 5), texture page A (9), texture page B (10), blend word (12), draw number (13), layer (14), priority (15), tile grid (17), animated frame (18)

## Notes

Our names. Tags: V.

## Open questions

- ?: opcodes 16 and 19..21 have unnamed handlers (sub_1403911B4, sub_140391AA4, sub_140391B04, sub_140391B68)
