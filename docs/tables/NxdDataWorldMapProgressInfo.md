# NxdDataWorldMapProgressInfo

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 123
- **Rows:** 91 rows of 44 bytes, text in 7 languages
- **Keyed by:** two keys: id (0..1000) x id2 (0..999)
- **Row layout:** [NxdDataWorldMapProgressInfoRow](../structs/NxdDataWorldMapProgressInfoRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

World-map progress steps keyed by group and step: towns, roads, caption and condition links. Verdict: designer-data.

## Behavior

- V: 91 rows, two keys id (0..1000) x id2 (0..999); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 11 columns not decoded (see the row layout)
