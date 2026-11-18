# LegacyItemUseLayoutLang2

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FD4D0`
- **Rows:** 1 script (0x100 bytes)
- **Keyed by:** text language
- **Read by:** [ClassicItemUsePage_Run](../functions/ClassicItemUsePage_Run.md)
- **Row layout:** [LegacyItemScriptRecord](../structs/LegacyItemScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layout script of the item use page of the legacy party menu (using an item on a unit), language 2 variant. The four blocks are interleaved with the item list blocks (stride 0x290). Verdict: designer-data.

## Behavior

- V: script bytes follow the item page runner's record shape (opcode first; end opcode 25); the reader picks the block by text language
- V: ClassicItemUsePage_Run (0x1403934B0): runs the item page script of the text language (0 at 0x1408FCFB0, 3 at 0x1408FD760, 2 at 0x1408FD4D0, default at 0x1408FD240)

## Notes

Our names. Tags: V reader, I screen, ? records.

## Open questions

- ?: what the tail pointers of the script object are (two heap-side buffers and window templates)
