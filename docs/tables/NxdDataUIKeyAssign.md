# NxdDataUIKeyAssign

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 25
- **Rows:** 256 rows of 48 bytes
- **Keyed by:** one key: id (0..255)
- **Row layout:** [NxdDataUIKeyAssignRow](../structs/NxdDataUIKeyAssignRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Key assignment table (256): main and alternate key codes. Verdict: engine-data.

## Behavior

- V: 256 rows, one key id (0..255); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 20 of 22 columns not decoded (see the row layout)
