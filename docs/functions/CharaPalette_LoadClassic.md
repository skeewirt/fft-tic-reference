# CharaPalette_LoadClassic

- **Address:** `0x14026E750`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void *CharaPalette_LoadClassic(int shape, uint16_t *pal)`
- **Callers:** CharaRender_BuildAtlasTexture
- **Callees:** GameData_ReadSectors, CharShape_ApplyClut, `sub_1402F3888` (scratch alloc), `sub_1402F3A04` (free)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a 256-colour palette (16 palettes of 16 colours) for a sprite shape from the shape's classic sprite file, then lets the shape's colour-override rows adjust it. The atlas builder calls it to get a unit's default colours.

## Behavior

- V: picks one of two identical {file kind, size} pair tables (indexed by shape) depending on the language info flag at +8 (0 selects the second table, a missing language record selects the first).
- V: allocates a scratch buffer of the table's size, reads the file with GameData_ReadSectors(kind, 0, size) and returns null if the allocation fails.
- V: copies the first 0x200 bytes of the file into the palette as 256 16-bit values. Every odd-numbered byte (the high byte of each colour) gets bit 0x80 set, except byte 1 of each 32-byte palette, so colour 0 of every palette stays without the opaque bit.
- V: then calls CharShape_ApplyClut(shape, pal) and releases the scratch buffer.
- I: the 16-bit values are BGR555 with the opaque flag in bit 15, matching the converter used by the atlas builder.
- V: has no direct caller other than CharaRender_BuildAtlasTexture (and a function-pointer table slot).

## State touched

- Calls: [GameData_ReadSectors](GameData_ReadSectors.md), [CharShape_ApplyClut](CharShape_ApplyClut.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Observed behaviours: [CharShapeKeyByteSites](../behaviors/CharShapeKeyByteSites.md), [EnhancedDrawsHdSheetsWithTheClassicFilePalette](../behaviors/EnhancedDrawsHdSheetsWithTheClassicFilePalette.md), [HdSheetAndClassicPaletteLoading](../behaviors/HdSheetAndClassicPaletteLoading.md), [SpriteSheetPortraitAndPartFiles](../behaviors/SpriteSheetPortraitAndPartFiles.md), [SpriteSheetsAndClassicFilesByNumber](../behaviors/SpriteSheetsAndClassicFilesByNumber.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md), [SpriteTablesEndAtSprite169](../behaviors/SpriteTablesEndAtSprite169.md)
- Resolves registries: [SpriteNumberTables](../registries/SpriteNumberTables.md)

## Notes

Both kind tables hold one {kind, size} pair per shape; sizes are multiples of 2048 (disc sector size).

No bound on the shape here (V): the row is read at table + 8 * shape. A row with size 0 allocates nothing to read and leaves the scratch buffer unread. CharShape_ApplyClut takes the shape as a byte.

## Open questions

None recorded.
