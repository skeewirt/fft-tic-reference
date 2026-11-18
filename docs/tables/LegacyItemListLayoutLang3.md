# LegacyItemListLayoutLang3

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FD860`
- **Rows:** 1 script (0x190 bytes)
- **Keyed by:** text language
- **Read by:** [ClassicItemListPage_Run](../functions/ClassicItemListPage_Run.md)
- **Row layout:** [LegacyItemScriptRecord](../structs/LegacyItemScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layout script of the item list page of the legacy party menu, language 3 variant. Each block contains a second script chunk at +0x100. Verdict: designer-data.

## Behavior

- V: script bytes follow the item page runner's record shape (opcode first; end opcode 25); the reader picks the block by text language
- V: ClassicItemListPage_Run (0x140393E70): picks the script by text language (0 at 0x1408FD0B0, 3 at 0x1408FD860, 2 at 0x1408FD5D0, default at 0x1408FD340) and a header chunk 0x100 bytes later

## Notes

Our names. Tags: V reader, I screen, ? records.

## Open questions

- ?: what the tail pointers of the script object are (two heap-side buffers and window templates)
