# NxdDataUIFontType

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 27
- **Rows:** 19 rows of 24 bytes
- **Keyed by:** one key: id (0..18)
- **Row layout:** [NxdDataUIFontTypeRow](../structs/NxdDataUIFontTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Font types (19) with file path. Verdict: engine-data.

## Behavior

- V: 19 rows, one key id (0..18); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 6 columns not decoded (see the row layout)
