# NxdDataDebugRefinedBgTexture

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 80
- **Rows:** 0 rows of 0 bytes
- **Keyed by:** three keys: id x id2 x id3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Debug triple-keyed table with no rows and no layout columns. Verdict: engine-data.

## Behavior

- V: 0 rows, three keys id x id2 x id3; measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); no rows and no layout columns in the retail file
