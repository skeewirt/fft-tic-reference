# LegacyItemListBodyGridA

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FD9F0`
- **Rows:** 1 grid (0x1280 bytes)
- **Keyed by:** cell index (row-major)
- **Read by:** [ClassicItemListPage_Run](../functions/ClassicItemListPage_Run.md)
- **Row layout:** [LegacyItemListBodyGridARow](../structs/LegacyItemListBodyGridARow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cell code grid of a large legacy list body (variant a). Verdict: designer-data.

## Behavior

- V: 0x1280 bytes up to the next object; codes are a small set
- V: ClassicItemListPage_Run (0x140393E70): one of two grids chosen by a page flag; the other is exe.ui.legacy_item_list_body_grid.b

## Notes

Our names. Tags: V reader, ? meaning.

## Open questions

- ?: row width and what the codes draw
