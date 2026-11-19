# NxdDataSeSystem

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 201
- **Rows:** 169 rows of 8 bytes
- **Keyed by:** one key: id (1..169)
- **Row layout:** [NxdDataSeSystemRow](../structs/NxdDataSeSystemRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

System sound effects (169). Verdict: engine-data.

## Behavior

- V: 169 rows, one key id (1..169); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 2 columns not decoded (see the row layout)
