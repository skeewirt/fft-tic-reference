# NxdDataUISubtitlesTimeline

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 142
- **Rows:** 94 rows of 24 bytes
- **Keyed by:** one key: id (1..20045)
- **Row layout:** [NxdDataUISubtitlesTimelineRow](../structs/NxdDataUISubtitlesTimelineRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Subtitle timelines (94). Verdict: engine-data.

## Behavior

- V: 94 rows, one key id (1..20045); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 6 of 6 columns not decoded (see the row layout)
