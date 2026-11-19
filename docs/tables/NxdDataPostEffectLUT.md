# NxdDataPostEffectLUT

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 285
- **Rows:** 31 rows of 20 bytes
- **Keyed by:** one key: id (0..30)
- **Row layout:** [NxdDataPostEffectLUTRow](../structs/NxdDataPostEffectLUTRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Colour lookup parameters (31). Verdict: engine-data.

## Behavior

- V: 31 rows, one key id (0..30); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 5 columns not decoded (see the row layout)
