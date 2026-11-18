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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 5 of 6 columns not decoded (see the row layout)
