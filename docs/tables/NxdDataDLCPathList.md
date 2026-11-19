# NxdDataDLCPathList

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 335
- **Rows:** 1 rows of 12 bytes
- **Keyed by:** one key: id (1..1)
- **Row layout:** [NxdDataDLCPathListRow](../structs/NxdDataDLCPathListRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A path list for downloadable content (one row). Verdict: engine-data.

## Behavior

- V: 1 rows, one key id (1..1); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
