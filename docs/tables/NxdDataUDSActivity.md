# NxdDataUDSActivity

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 313
- **Rows:** 74 rows of 28 bytes
- **Keyed by:** one key: id (0..73)
- **Row layout:** [NxdDataUDSActivityRow](../structs/NxdDataUDSActivityRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Activity records for the platform's activity feed (74). Verdict: engine-data.

## Behavior

- V: 74 rows, one key id (0..73); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 3 of 5 columns not decoded (see the row layout)
