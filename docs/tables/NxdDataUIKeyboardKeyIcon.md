# NxdDataUIKeyboardKeyIcon

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 332
- **Rows:** 167 rows of 8 bytes
- **Keyed by:** one key: id (0..166)
- **Row layout:** [NxdDataUIKeyboardKeyIconRow](../structs/NxdDataUIKeyboardKeyIconRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Keyboard key icon map (167). Verdict: engine-data.

## Behavior

- V: 167 rows, one key id (0..166); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 1 of 2 columns not decoded (see the row layout)
