# NxdDataCaptionFreeWord

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 86
- **Rows:** 8 rows of 12 bytes, text in 7 languages
- **Keyed by:** one key: id (0..20)
- **Row layout:** [NxdDataCaptionFreeWordRow](../structs/NxdDataCaptionFreeWordRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Free-form caption words used by the caption system. Verdict: text.

## Behavior

- V: 8 rows, one key id (0..20); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
