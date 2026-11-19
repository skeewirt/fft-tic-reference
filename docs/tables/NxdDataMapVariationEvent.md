# NxdDataMapVariationEvent

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 207
- **Rows:** 14 rows of 20 bytes
- **Keyed by:** one key: id (0..13)
- **Row layout:** [NxdDataMapVariationEventRow](../structs/NxdDataMapVariationEventRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Map variations tied to events (14). Verdict: designer-data.

## Behavior

- V: 14 rows, one key id (0..13); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 4 columns not decoded (see the row layout)
