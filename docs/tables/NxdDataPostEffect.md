# NxdDataPostEffect

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 228
- **Rows:** 2 rows of 16 bytes
- **Keyed by:** one key: id (0..1)
- **Row layout:** [NxdDataPostEffectRow](../structs/NxdDataPostEffectRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two post effect definitions with an effect file path. Verdict: engine-data.

## Behavior

- V: 2 rows, one key id (0..1); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 4 columns not decoded (see the row layout)
