# NxdDataRefinedBgSystemTexture

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 141
- **Rows:** 870 rows of 24 bytes
- **Keyed by:** three keys: id (1..116) x id2 (0..0) x id3 (0..7)
- **Row layout:** [NxdDataRefinedBgSystemTextureRow](../structs/NxdDataRefinedBgSystemTextureRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

System textures of remastered backgrounds, triple keyed. Verdict: engine-data.

## Behavior

- V: 870 rows, three keys id (1..116) x id2 (0..0) x id3 (0..7); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
