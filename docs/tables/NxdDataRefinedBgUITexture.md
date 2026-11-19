# NxdDataRefinedBgUITexture

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 223
- **Rows:** 20 rows of 20 bytes
- **Keyed by:** one key: id (0..19)
- **Row layout:** [NxdDataRefinedBgUITextureRow](../structs/NxdDataRefinedBgUITextureRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI textures of remastered backgrounds, with frame id arrays. Verdict: engine-data.

## Behavior

- V: 20 rows, one key id (0..19); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 6 columns not decoded (see the row layout)
