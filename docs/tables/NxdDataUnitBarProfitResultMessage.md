# NxdDataUnitBarProfitResultMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 205
- **Rows:** 240 rows of 12 bytes
- **Keyed by:** two keys: id (21..50) x id2 (0..7)
- **Row layout:** [NxdDataUnitBarProfitResultMessageRow](../structs/NxdDataUnitBarProfitResultMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Errand result message voice entries keyed by errand and slot. Verdict: designer-data.

## Behavior

- V: 240 rows, two keys id (21..50) x id2 (0..7); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
