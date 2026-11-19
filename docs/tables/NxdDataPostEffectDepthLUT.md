# NxdDataPostEffectDepthLUT

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 284
- **Rows:** 30 rows of 40 bytes
- **Keyed by:** one key: id (0..29)
- **Row layout:** [NxdDataPostEffectDepthLUTRow](../structs/NxdDataPostEffectDepthLUTRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Depth lookup parameters (30). Verdict: engine-data.

## Behavior

- V: 30 rows, one key id (0..29); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 10 of 10 columns not decoded (see the row layout)
