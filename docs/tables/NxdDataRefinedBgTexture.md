# NxdDataRefinedBgTexture

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 71
- **Rows:** 1338 rows of 40 bytes
- **Keyed by:** three keys: id (0..116) x id2 (0..17) x id3 (0..2)
- **Row layout:** [NxdDataRefinedBgTextureRow](../structs/NxdDataRefinedBgTextureRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Textures of remastered backgrounds, triple keyed (1338 rows). Verdict: engine-data.

## Behavior

- V: 1338 rows, three keys id (0..116) x id2 (0..17) x id3 (0..2); measured over every row of the stock file.
- V: read by MapTextures_NameOfFrame through the table id 71: the key is (map id, slot below 21, type 0 colour / 1 lighting / 2 other); the row holds two pairs of a name list and a frame-count list.
- V: over all 1,338 rows every name resolves to a texture file in the texture folder of its map once a frame series is expanded by its count (frame k replaces the final 0 of the name by k), file names compared without case; the only misses are names of map 0, which has no mesh.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 6 of 6 columns not decoded (see the row layout)
