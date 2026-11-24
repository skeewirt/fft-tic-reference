# NxdDataDebugMap

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 78
- **Rows:** 80 rows of 16 bytes
- **Keyed by:** one key: id (0..79)
- **Row layout:** [NxdDataDebugMapRow](../structs/NxdDataDebugMapRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Debug map list (80 rows) with comment text. Verdict: engine-data.

## Behavior

- V: 80 rows, one key id (0..79); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Referenced by

- Observed behaviours: [DebugSceneTablesShipStripped](../behaviors/DebugSceneTablesShipStripped.md)

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 4 columns not decoded (see the row layout)
