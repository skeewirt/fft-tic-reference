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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 5 columns not decoded (see the row layout)
