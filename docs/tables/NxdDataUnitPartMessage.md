# NxdDataUnitPartMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 191
- **Rows:** 59 rows of 12 bytes
- **Keyed by:** two keys: id (3..99) x id2 (0..0)
- **Row layout:** [NxdDataUnitPartMessageRow](../structs/NxdDataUnitPartMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit part message voice entries. Verdict: designer-data.

## Behavior

- V: 59 rows, two keys id (3..99) x id2 (0..0); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
