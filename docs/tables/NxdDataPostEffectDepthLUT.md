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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 8 of 10 columns not decoded (see the row layout)
