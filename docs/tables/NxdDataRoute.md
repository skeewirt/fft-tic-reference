# NxdDataRoute

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 97
- **Rows:** 51 rows of 28 bytes
- **Keyed by:** one key: id (0..50)
- **Row layout:** [NxdDataRouteRow](../structs/NxdDataRouteRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Road records (51): parameters of world-map roads. Verdict: designer-data.

## Behavior

- V: 51 rows, one key id (0..50); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 6 of 7 columns not decoded (see the row layout)
