# NxdDataGuidePage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 188
- **Rows:** 409 rows of 24 bytes, text in 7 languages
- **Keyed by:** two keys: id (0..3277) x id2 (0..7)
- **Read by:** [GuideWindow_ShowPage](../functions/GuideWindow_ShowPage.md)
- **Row layout:** [NxdDataGuidePageRow](../structs/NxdDataGuidePageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Guide pages keyed by guide id and page index: icon id arrays and text slots. Verdict: designer-data.

## Behavior

- V: 409 rows, two keys id (0..3277) x id2 (0..7); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 5 columns not decoded (see the row layout)
