# NxdDataRefinedPermanentVFX

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 321
- **Rows:** 21 rows of 12 bytes
- **Keyed by:** one key: id (1..21)
- **Row layout:** [NxdDataRefinedPermanentVFXRow](../structs/NxdDataRefinedPermanentVFXRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Permanent effect definitions (21). Verdict: engine-data.

## Behavior

- V: 21 rows, one key id (1..21); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
