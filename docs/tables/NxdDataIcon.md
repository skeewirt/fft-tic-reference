# NxdDataIcon

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 118
- **Rows:** 1400 rows of 16 bytes
- **Keyed by:** one key: id (0..1399)
- **Row layout:** [NxdDataIconRow](../structs/NxdDataIconRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Icon id to image file path (1400 rows). Verdict: engine-data.

## Behavior

- V: 1400 rows, one key id (0..1399); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 1 of 4 columns not decoded (see the row layout)
