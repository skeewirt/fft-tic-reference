# NxdDataUIDialog

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 34
- **Rows:** 241 rows of 60 bytes
- **Keyed by:** one key: id (0..240)
- **Row layout:** [NxdDataUIDialogRow](../structs/NxdDataUIDialogRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Dialog definitions (241): text and option UI text keys. Verdict: designer-data.

## Behavior

- V: 241 rows, one key id (0..240); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 11 of 15 columns not decoded (see the row layout)
