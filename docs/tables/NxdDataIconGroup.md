# NxdDataIconGroup

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 29
- **Rows:** 75 rows of 12 bytes
- **Keyed by:** one key: id (0..74)
- **Row layout:** [NxdDataIconGroupRow](../structs/NxdDataIconGroupRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Icon group parameters (75 rows). Verdict: engine-data.

## Behavior

- V: 75 rows, one key id (0..74); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 5 of 6 columns not decoded (see the row layout)
