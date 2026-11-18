# UiLegacyWindowCellLayoutBase

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140813AB0`
- **Rows:** about 81 rows of 12 bytes
- **Keyed by:** cell index
- **Row layout:** [WindowCellRecordRow](../structs/WindowCellRecordRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cell records (kind, size, offset) of a legacy list window, base set. Verdict: designer-data.

## Behavior

- V: read by sub_1402CB054, which also takes a language-dependent set

## Notes

Our names. Tags: I stride, ? count.

## Open questions

- ?: exact cell count
