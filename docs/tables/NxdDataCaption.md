# NxdDataCaption

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 87
- **Rows:** 13 rows of 16 bytes
- **Keyed by:** one key: id (0..1300)
- **Row layout:** [NxdDataCaptionRow](../structs/NxdDataCaptionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Caption slots whose content is a typed reference (union) to another table's row. Verdict: engine-data.

## Behavior

- V: 13 rows, one key id (0..1300); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id)
