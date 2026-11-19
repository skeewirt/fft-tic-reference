# NxdDataContinuousBattleTimeline

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 231
- **Rows:** 46 rows of 8 bytes
- **Keyed by:** one key: id (0..45)
- **Row layout:** [NxdDataContinuousBattleTimelineRow](../structs/NxdDataContinuousBattleTimelineRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Timeline steps for chained battles (46 rows). Verdict: engine-data.

## Behavior

- V: 46 rows, one key id (0..45); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 2 columns not decoded (see the row layout)
