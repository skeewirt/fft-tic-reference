# NxdDataPostEffectDOF

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 227
- **Rows:** 34 rows of 28 bytes
- **Keyed by:** one key: id (1..34)
- **Row layout:** [NxdDataPostEffectDOFRow](../structs/NxdDataPostEffectDOFRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Depth-of-field parameters (34). Verdict: engine-data.

## Behavior

- V: 34 rows, one key id (1..34); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 5 of 7 columns not decoded (see the row layout)
