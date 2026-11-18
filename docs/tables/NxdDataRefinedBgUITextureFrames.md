# NxdDataRefinedBgUITextureFrames

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 222
- **Rows:** 17 rows of 12 bytes
- **Keyed by:** two keys: id (0..16) x id2 (0..0)
- **Row layout:** [NxdDataRefinedBgUITextureFramesRow](../structs/NxdDataRefinedBgUITextureFramesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Frame texture file paths of background UI textures. Verdict: engine-data.

## Behavior

- V: 17 rows, two keys id (0..16) x id2 (0..0); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
