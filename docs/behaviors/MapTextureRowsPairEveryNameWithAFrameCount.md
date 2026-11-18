# MapTextureRowsPairEveryNameWithAFrameCount

- **Kind:** observed behaviour
- **Scope:** engine (map texture rows)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapTextures_NameOfFrame](../functions/MapTextures_NameOfFrame.md), [MapTextures_LoadMapSlots](../functions/MapTextures_LoadMapSlots.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A RefinedBgTexture row has two name lists and, beside each, a list of frame counts stored as plain signed 32-bit integers. The name builder reads the count at the name's index and returns no name unless the frame number is below it, so a name with no count, or a count of 0, is never requested and its texture is missing.

## Behavior

- V: the row has four array fields at +8, +16, +24 and +32: names (text offsets), counts (int32), names, counts; the first pair is read at the map variation index, the second at the kind-code index.
- V (data): in all 1,338 stock rows the second count array has as many elements as the second name array (values 1, 5, 8, 10 or 30), and the first pair is equal in length except for one row with no names and one count.
- V (data): with a frame series expanded by its counts (frame k replaces the final 0 of the name by k), every name of every stock row resolves to a file of its map's texture folder, file names compared without case; the exceptions are the names of map 0, which has no mesh.
- V: the count 1 (bytes 01 00 00 00), read as an offset to text, points at the array's own second byte, a NUL: the cell is a valid reference to an empty string, so the bytes alone do not tell it from text (the type is known only from the reader's code).

## Notes

Seen live: with the counts missing the map's terrain textures were never requested (no texture file of the map was asked for); with the stock counts they were.

## Open questions

None recorded.
