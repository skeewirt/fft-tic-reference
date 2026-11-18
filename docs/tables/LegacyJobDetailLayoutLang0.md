# LegacyJobDetailLayoutLang0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FC760`
- **Rows:** 1 script (0x1F0 bytes)
- **Keyed by:** text language
- **Read by:** [ClassicJobDetailPage_Run](../functions/ClassicJobDetailPage_Run.md)
- **Row layout:** [LegacyUiScriptRecord](../structs/LegacyUiScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layout script of the job detail page of the legacy party menu (four pages of the chosen job), language 0 variant. The language 3 block is 0x90 bytes longer because a small table follows it. Verdict: designer-data.

## Behavior

- V: script bytes follow the record shape the runner ClassicUi_RunLayoutScript reads; the reader picks the block by text language
- V: ClassicJobDetailPage_Run (0x140392DB8): runs the script of the text language (0 at 0x1408FC760, 3 at 0x1408FCD30, 2 at 0x1408FCB40, default at 0x1408FC950) then draws a fixed corner cell

## Notes

Our names. Tags: V reader, I screen, ? records.

## Open questions

- ?: what the tail pointers of the script object are (two heap-side buffers and window templates)
