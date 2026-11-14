# SpriteSheetEntries

- **Kind:** file format
- **Extension:** `(g2d entries)`
- **Area:** [Graphics](../areas/graphics.md)
- **Read by:** [PackFile_ReadEntry](../functions/PackFile_ReadEntry.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md), [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [HdGroup_BuildPiece](../functions/HdGroup_BuildPiece.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The sprite data of a unit look: two HD sheet entries, the classic sprite file and its palette rows.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="sheet rows 0..511"></a>HD sheet entry 0 | sheet rows 0..511 | `512 x 512 pixels` | V | The first HD sheet entry as the game holds it inflated: 4 bits per pixel (131072 bytes, low nibble = left pixel), or 8 bits per pixel (262144 bytes) for the sheet groups the battle layer builds with 256 colours. Pixel = colour number, 0 transparent. |
| <a id="sheet rows 512..975"></a>HD sheet entry 1 | sheet rows 512..975 | `512 x 464 pixels` | V | The second entry: 118784 bytes at 4 bits, 237568 bytes at 8 bits. |
| <a id="classic sprite file"></a>classic sprite file | classic sprite file | `bytes` | V | The classic file: its first 0x200 bytes are 16 rows of 16 colours (u16, 5 bits red, green, blue from the low bit). These rows are what the game loads, tints and fades. |

## Behavior

- V: the sheets are the classic 256 x 488 sheet drawn at twice the size; which rectangles of it a frame uses comes from the frame files.

## Open questions

None recorded.
