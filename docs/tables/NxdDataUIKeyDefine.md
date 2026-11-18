# NxdDataUIKeyDefine

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 35
- **Rows:** 256 rows of 32 bytes
- **Keyed by:** one key: id (0..255)
- **Row layout:** [NxdDataUIKeyDefineRow](../structs/NxdDataUIKeyDefineRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Key definition table (256). Verdict: engine-data.

## Behavior

- V: 256 rows, one key id (0..255); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 6 of 8 columns not decoded (see the row layout)
