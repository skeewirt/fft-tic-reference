# LegacyJobChoiceLayoutLang3

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FC650`
- **Rows:** 1 script (0x110 bytes)
- **Keyed by:** text language
- **Row layout:** [LegacyUiScriptRecord](../structs/LegacyUiScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layout script of the job choice page of the legacy party menu (the page that lists a unit's jobs and applies a change), language 3 variant.  Verdict: designer-data.

## Behavior

- V: script bytes follow the record shape the runner ClassicUi_RunLayoutScript reads; the reader picks the block by text language
- V: sub_14039297C (0x14039297C): runs the script of the text language (0 at 0x1408FC320, 3 at 0x1408FC650, 2 at 0x1408FC540, default at 0x1408FC430) when the page redraws

## Notes

Our names. Tags: V reader, I screen, ? records.

## Open questions

- ?: what the tail pointers of the script object are (two heap-side buffers and window templates)
