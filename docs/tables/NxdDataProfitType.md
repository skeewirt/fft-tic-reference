# NxdDataProfitType

- **Kind:** table
- **Area:** [Errands](../areas/errands.md)
- **Storage:** NXD file
- **NXD table id:** 243
- **Rows:** 8 rows of 20 bytes
- **Keyed by:** one key: id (1..8)
- **Row layout:** [NxdDataProfitTypeRow](../structs/NxdDataProfitTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Errand types (8) with three bonus item links. Verdict: designer-data.

## Behavior

- V: 8 rows, one key id (1..8); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 5 columns not decoded (see the row layout)
