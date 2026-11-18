# StatusPanelLayoutsLanguage0

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140808680`
- **Rows:** 8 rows of 8 bytes
- **Keyed by:** panel kind 0..7
- **Row layout:** [LayoutPointer](../structs/LayoutPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per status panel kind, its layout block, language 0. Verdict: pointer-table.

## Behavior

- V: 8 pointers; the next language table starts at +0x40
- V: Battle_UnitStatusFillAlt: layout = table[kind]; copies of the table for the other languages at 0x1408086C0 / 0x140808700 / 0x140808740

## Notes

Our names. Tags: V.

## Open questions

- ?: layout block format
