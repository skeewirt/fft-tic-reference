# LegacyTask13LayoutMode13

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FF8E0`
- **Rows:** 1 block (0x1C0 bytes)
- **Keyed by:** party menu page mode
- **Row layout:** [LegacyUiScriptRecord](../structs/LegacyUiScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layout block of the legacy scene task 13 for mode 13. Verdict: designer-data.

## Behavior

- V: reader selects between 0x1408FF8E0 (mode 13) and 0x1408FFAA0 by the page mode word; 0x1C0 bytes each
- V: sub_1403980AC (0x1403980AC): selects this block for mode 13

## Notes

Our names. Tags: V reader, ? fields.

## Open questions

- ?: what the tail pointers of the script object are (two heap-side buffers and window templates)
