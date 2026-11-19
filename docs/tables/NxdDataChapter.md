# NxdDataChapter

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 206
- **Rows:** 6 rows of 16 bytes, text in 7 languages
- **Keyed by:** one key: id (1..6)
- **Read by:** [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md)
- **Row layout:** [NxdDataChapterRow](../structs/NxdDataChapterRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The six chapter titles with a story-progress number each. Verdict: designer-data.

## Behavior

- V: 6 rows, one key id (1..6); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 4 columns not decoded (see the row layout)
