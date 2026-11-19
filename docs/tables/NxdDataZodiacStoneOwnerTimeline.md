# NxdDataZodiacStoneOwnerTimeline

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** NXD file
- **NXD table id:** 238
- **Rows:** 11 rows of 16 bytes
- **Keyed by:** one key: id (0..10)
- **Row layout:** [NxdDataZodiacStoneOwnerTimelineRow](../structs/NxdDataZodiacStoneOwnerTimelineRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Zodiac stone owner timelines (11). Verdict: designer-data.

## Behavior

- V: 11 rows, one key id (0..10); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 4 columns not decoded (see the row layout)
