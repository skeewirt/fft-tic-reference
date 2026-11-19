# NxdDataNovelIcon

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 220
- **Rows:** 131 rows of 20 bytes
- **Keyed by:** one key: id (0..130)
- **Row layout:** [NxdDataNovelIconRow](../structs/NxdDataNovelIconRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Icons of the novel pages (131). Verdict: designer-data.

## Behavior

- V: 131 rows, one key id (0..130); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 5 columns not decoded (see the row layout)
