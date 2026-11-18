# LegacyTask12LayoutLang0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140900EC0`
- **Rows:** 1 script (0x110 bytes)
- **Keyed by:** text language
- **Read by:** [LegacyTask12_Build](../functions/LegacyTask12_Build.md)
- **Row layout:** [LegacyUiScriptRecord](../structs/LegacyUiScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cell list of the legacy scene task 12, language 0 variant. The records are six-word sprite cells (the shape of exe.ui.msg_window_tag_cells). Verdict: designer-data.

## Behavior

- V: script bytes follow the record shape the runner ClassicUi_RunLayoutScript reads; the reader picks the block by text language
- V: LegacyTask12_Build (0x14039A518): chooses the block by text language (0 at 0x140900EC0, 3 at 0x1409011F0, 2 at 0x1409010E0, default at 0x140900FD0) and copies its 17 cell records

## Notes

Our names. Tags: V reader, I screen, ? records.

## Open questions

- ?: what the tail pointers of the script object are (two heap-side buffers and window templates)
