# NxdDataUIKeyDefine

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 35
- **Rows:** 256 rows of 32 bytes
- **Keyed by:** one key: id (0..255)
- **Row layout:** [NxdDataUIKeyDefineRow](../structs/NxdDataUIKeyDefineRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Key definition table (256). Verdict: engine-data.

## Behavior

- V: 256 rows, one key id (0..255); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 8 of 8 columns not decoded (see the row layout)
