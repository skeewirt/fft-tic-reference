# LegacyMenuRowListPointers

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406802F0`
- **Rows:** 48 rows of 8 bytes
- **Keyed by:** menu id 0..47
- **Read by:** [LegacyMenu_LoadRowList](../functions/LegacyMenu_LoadRowList.md)
- **Row layout:** [LegacyMenuRowListPointersRow](../structs/LegacyMenuRowListPointersRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointers to the byte lists of row ids of each legacy menu; the matching row counts are LegacyMenuRowCounts. Verdict: pointer-table.

## Behavior

- V: the run of valid pointers has 50 entries, but the byte count table has 48; slots 48 and 49 are not indexed by any menu id (they repeat the targets of slots 38 and 39), so the table is 48 rows
- V: the targets are short byte lists packed one behind the other, and several lists overlap
- V: the pointed-to lists live in the initialised data section and are only read by the loader (seen: a list of 10 rows at 0x140789540)

## Notes

Our names. Tags: V layout, V reader.

## Open questions

None recorded.
