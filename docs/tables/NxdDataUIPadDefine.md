# NxdDataUIPadDefine

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 28
- **Rows:** 61 rows of 16 bytes
- **Keyed by:** one key: id (0..60)
- **Row layout:** [NxdDataUIPadDefineRow](../structs/NxdDataUIPadDefineRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pad button definitions (61). Verdict: engine-data.

## Behavior

- V: 61 rows, one key id (0..60); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 3 of 4 columns not decoded (see the row layout)
