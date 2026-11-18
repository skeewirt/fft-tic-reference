# LegacyMenuRowCounts

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406804B0`
- **Rows:** 48 rows of 1 byte
- **Keyed by:** menu id 0..47
- **Read by:** [LegacyMenu_LoadRowList](../functions/LegacyMenu_LoadRowList.md)
- **Row layout:** [LegacyMenuRowCountsRow](../structs/LegacyMenuRowCountsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number of rows of each legacy menu (the list is LegacyMenuRowListPointers). Verdict: designer-data.

## Behavior

- V: a count of 7 or more splits into a page of 7 and the remainder, stored in two words of the menu state

## Notes

Our names. Tags: V layout, V reader.

## Open questions

None recorded.
