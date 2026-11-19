# NxdDataUISubtitlesComponent

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 162
- **Rows:** 79 rows of 16 bytes
- **Keyed by:** one key: id (1..79)
- **Row layout:** [NxdDataUISubtitlesComponentRow](../structs/NxdDataUISubtitlesComponentRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Subtitle window components (79). Verdict: engine-data.

## Behavior

- V: 79 rows, one key id (1..79); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 4 columns not decoded (see the row layout)
