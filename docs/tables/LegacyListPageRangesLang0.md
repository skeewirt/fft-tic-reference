# LegacyListPageRangesLang0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FBCD0`
- **Rows:** 120 rows of 2 bytes
- **Keyed by:** category
- **Read by:** [ClassicListPage_BuildRangeList](../functions/ClassicListPage_BuildRangeList.md)
- **Row layout:** [ListPageRangeStart](../structs/ListPageRangeStart.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cumulative start ids that cut a long entry list (names of the legacy list page) into categories; language 0 variant. Verdict: designer-data.

## Behavior

- V: ranges are monotonic from 0x0B to about 0x266; the reader copies the ids of the range into a 0xFFFF-terminated list and hands it to the list drawer
- V: ClassicListPage_BuildRangeList (0x14037B8FC): list = the ids start .. end - 1 of range [category], [category + 1]; the block is chosen by text language (0 at 0x1408FBCD0, 1 at 0x1408FBDC0, 3 at 0x1408FBEB0, 2 at 0x1408FBFA0)

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: what the entries are (the list contains up to 0x266 ids)
