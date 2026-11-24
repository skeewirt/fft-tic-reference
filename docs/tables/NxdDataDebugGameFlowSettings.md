# NxdDataDebugGameFlowSettings

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 102
- **Rows:** 0 rows of 0 bytes
- **Keyed by:** two keys: id x id2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Debug table with no rows and no layout columns in the retail file. Verdict: engine-data.

## Behavior

- V: 0 rows, two keys id x id2; measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Referenced by

- Observed behaviours: [DebugSceneTablesShipStripped](../behaviors/DebugSceneTablesShipStripped.md)

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); no rows and no layout columns in the retail file
