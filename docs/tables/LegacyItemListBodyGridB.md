# LegacyItemListBodyGridB

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FEC70`
- **Rows:** 1 grid (0xBA0 bytes)
- **Keyed by:** cell index (row-major)
- **Read by:** [ClassicItemListPage_Run](../functions/ClassicItemListPage_Run.md)
- **Row layout:** [LegacyItemListBodyGridBRow](../structs/LegacyItemListBodyGridBRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cell code grid of a large legacy list body (variant b). Verdict: designer-data.

## Behavior

- V: 0xBA0 bytes up to the next object
- V: ClassicItemListPage_Run (0x140393E70): the alternative grid

## Notes

Our names. Tags: V reader, ? meaning.

## Open questions

- ?: row width and what the codes draw
