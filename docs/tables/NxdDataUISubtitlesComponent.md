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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
