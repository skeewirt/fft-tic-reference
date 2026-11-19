# NxdDataSystemBonusItemContents

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 296
- **Rows:** 12 rows of 12 bytes
- **Keyed by:** two keys: id (1..2) x id2 (0..6)
- **Row layout:** [NxdDataSystemBonusItemContentsRow](../structs/NxdDataSystemBonusItemContentsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bonus item contents, keyed by bonus and slot, typed references. Verdict: designer-data.

## Behavior

- V: 12 rows, two keys id (1..2) x id2 (0..6); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
