# NxdDataUIKeyboardType

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 327
- **Rows:** 6 rows of 28 bytes
- **Keyed by:** one key: id (1..6)
- **Row layout:** [NxdDataUIKeyboardTypeRow](../structs/NxdDataUIKeyboardTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Keyboard types (6). Verdict: engine-data.

## Behavior

- V: 6 rows, one key id (1..6); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 7 of 7 columns not decoded (see the row layout)
