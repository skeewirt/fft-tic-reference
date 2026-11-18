# NxdDataChapterFile

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 239
- **Rows:** 13 rows of 8 bytes
- **Keyed by:** one key: id (0..12)
- **Row layout:** [NxdDataChapterFileRow](../structs/NxdDataChapterFileRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Maps chapter file slots to chapter numbers. Verdict: engine-data.

## Behavior

- V: 13 rows, one key id (0..12); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 1 of 3 columns not decoded (see the row layout)
