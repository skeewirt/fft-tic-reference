# NxdDataJournal

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 122
- **Rows:** 117 rows of 40 bytes, text in 7 languages
- **Keyed by:** one key: id (10..1112)
- **Row layout:** [NxdDataJournalRow](../structs/NxdDataJournalRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Journal entries (117): story-progress condition, title and text. Verdict: designer-data.

## Behavior

- V: 117 rows, one key id (10..1112); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 9 of 12 columns not decoded (see the row layout)
