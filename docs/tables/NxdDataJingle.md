# NxdDataJingle

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 319
- **Rows:** 11 rows of 12 bytes
- **Keyed by:** one key: id (0..10)
- **Row layout:** [NxdDataJingleRow](../structs/NxdDataJingleRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Eleven jingles pointing at sound resources. Verdict: engine-data.

## Behavior

- V: 11 rows, one key id (0..10); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
