# NxdDataMap

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 60
- **Rows:** 129 rows of 32 bytes
- **Keyed by:** one key: id (0..128)
- **Row layout:** [NxdDataMapRow](../structs/NxdDataMapRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per map (129): parameters; map content lives in map files. Verdict: designer-data.

## Behavior

- V: 129 rows, one key id (0..128); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 7 of 7 columns not decoded (see the row layout)
