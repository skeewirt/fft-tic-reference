# NxdDataScionFiles

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 169
- **Rows:** 498 rows of 8 bytes
- **Keyed by:** one key: id (1000..2164)
- **Row layout:** [NxdDataScionFilesRow](../structs/NxdDataScionFilesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

File names of the voice archives (498). Verdict: engine-data.

## Behavior

- V: 498 rows, one key id (1000..2164); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
