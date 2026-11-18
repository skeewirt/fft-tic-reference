# NxdDataAchievementArray

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 213
- **Rows:** 7 rows of 28 bytes
- **Keyed by:** one key: id (0..6)
- **Row layout:** [NxdDataAchievementArrayRow](../structs/NxdDataAchievementArrayRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Seven achievement groupings: arrays of achievement ids per group. Verdict: engine-data.

## Behavior

- V: 7 rows, one key id (0..6); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
