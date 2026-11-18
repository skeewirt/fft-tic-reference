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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
