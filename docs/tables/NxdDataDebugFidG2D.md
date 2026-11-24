# NxdDataDebugFidG2D

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 212
- **Rows:** 1285 rows of 12 bytes
- **Keyed by:** one key: id (0..1284)
- **Row layout:** [NxdDataDebugFidG2DRow](../structs/NxdDataDebugFidG2DRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Debug 2D resource id list (1285 rows). Verdict: engine-data.

## Behavior

- V: 1285 rows, one key id (0..1284); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Referenced by

- Observed behaviours: [DebugSceneTablesShipStripped](../behaviors/DebugSceneTablesShipStripped.md)

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
