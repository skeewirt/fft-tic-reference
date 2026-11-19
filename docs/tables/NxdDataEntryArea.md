# NxdDataEntryArea

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 244
- **Rows:** 2519 rows of 8 bytes
- **Keyed by:** two keys: id (256..722) x id2 (0..19)
- **Row layout:** [NxdDataEntryAreaRow](../structs/NxdDataEntryAreaRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Deployment areas: per battle and slot, a position value. Verdict: designer-data.

## Behavior

- V: 2519 rows, two keys id (256..722) x id2 (0..19); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 2 columns not decoded (see the row layout)
