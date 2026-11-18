# NxdDataUIFontSet

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 21
- **Rows:** 100 rows of 100 bytes
- **Keyed by:** one key: id (0..99)
- **Row layout:** [NxdDataUIFontSetRow](../structs/NxdDataUIFontSetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Font sets (100) as groups of font type ids. Verdict: engine-data.

## Behavior

- V: 100 rows, one key id (0..99); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 16 of 25 columns not decoded (see the row layout)
