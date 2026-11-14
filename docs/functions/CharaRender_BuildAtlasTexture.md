# CharaRender_BuildAtlasTexture

- **Address:** `0x1400CE204`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void *CharaRender_BuildAtlasTexture(__int64 unused, int width, unsigned shape, int which, short palA, short palB, int flags)`
- **Callers:** CharaRender_DrawFrame (0x1400CD458)
- **Callees:** sub_1403D2450, sub_1403D25D8 (pack read), sub_14026E750 / sub_14026C530 (default palettes), sub_1402F3888 / sub_1402F40C4 / sub_1402F3A04 (palette overlays), Rgb555ToRgba8888, sub_1403D0898 / sub_1403D0A80 / sub_1403D0B10 (texture create/upload/finish), sub_140011750 / sub_140011804 (alloc/free)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the unit's atlas texture: loads the shape's sprite file from the FFT pack, applies the 16-colour palette (with optional colour offsets), and expands the 4-bit pixels into a 512 x 512 RGBA texture.

## Behavior

- V: file index = dword_1407151F0[shape] + which (which = 0/1: two textures per slot); shapes 155..158 use index 160 + which; flag bits 0x8000000 -> 1146, 0x60000000 -> 154, 0x10000000 -> 156 pick other sheets. The file is read through the pack (sub_1403D2450/sub_1403D25D8) into a 1 MB buffer. V (data): the index is the g2d.dat entry number: entry n is a 131072-byte (512 x 512, 4 bpp) sheet and entry n + 1 a 118784-byte (512 x 464) sheet, together the 2x redrawn HD version of the classic 256 x 488 sheet.
- V: palette entries are RGB555 (PSX); flag-selected modes (v30 = 4: add per-channel offsets; 5: 4-bit channels with offsets, I: a darkened variant; 6: grey (r + 3g + 2b)/6) clamp at 31 and keep colour 0 transparent; with no flags the offsets are 0 and the palette passes through unchanged; then Rgb555ToRgba8888 turns each into RGBA8888.
- V: texture = 512 rows x 256 source bytes (each byte = two 4-bit pixels, low nibble first, expanded through a 256-entry pair table), uploaded with sub_1403D0A80(tex, buf, 512, 512, 32 bpp): the sheet is exactly one g2d entry, indexed 4 bpp with the unit palette applied here.
- V: the default palette comes from CharaPalette_LoadClassic(shape, ...) (classic sprite file palette plus the shape's colour-override rows via CharClut_ApplyToPalette).
- V: a shape above 169 gets no sheet entry (index -1) unless a flag bit selects a special sheet; with no entry the function returns null.
- V: its tint lines are the battle rule's (UnitClut_TintRow): flag bit 0 grey; bit 1 grey with offsets 3, -1, 8; bit 2 plain with red + 8; bit 3 halved with green + 8; bit 4 halved with blue + 8; bit 5 halved with -4; bit 6 halved with -8; bit 7 (not for shapes 139 and 140) halved with 4, 0, 5; each channel limited to 0..31 and blue 1 for a colour that came out black.
- V: both of its outputs are 32-bit: the 16 converted colours (Rgb555ToRgba8888) and the 512 x 512 buffer handed to TextureObj_SetSource with depth 32. So the 16-colour limit of the menus is this expansion and nothing after it.

## State touched

- Calls: [sub_1403D2450](sub_1403D2450.md), [Rgb555ToRgba8888](Rgb555ToRgba8888.md), [sub_1403D0898](sub_1403D0898.md)

## Referenced by

- Called by: [CharaRender_DrawFrame](CharaRender_DrawFrame.md)
- Observed behaviours: [HdSheetAndClassicPaletteLoading](../behaviors/HdSheetAndClassicPaletteLoading.md), [SixteenColourLimitIsTwoCpuBuilders](../behaviors/SixteenColourLimitIsTwoCpuBuilders.md), [SpriteNumberStoreWidths](../behaviors/SpriteNumberStoreWidths.md), [SpriteSheetPortraitAndPartFiles](../behaviors/SpriteSheetPortraitAndPartFiles.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md)
- Reads file formats: [SpriteSheetEntries](../formats/SpriteSheetEntries.md)
- Resolves registries: [SpriteNumberTables](../registries/SpriteNumberTables.md)

## Notes

The pixels come from the HD sheets in g2d.dat, NOT from the classic 0002.pac sheets; quad UVs are classic px / 256, so one classic px spans 2 texels. The palette is the classic sheet's RGB555 palette (colours checked against retail).

The shape argument is unsigned 32-bit and the bound is an unsigned compare with 0xA9 at 0x1400CE263 (V): a shape above it takes the -1 path (no sheet unless a flag picks one). The menu record and the renderer slot cache hand the shape over as 32 bits, so this is the menu path's only look-number bound here.

The palette loaders are CharaPalette_LoadClassic, CharShape_ApplyClut and CharClut_ApplyToPalette.

## Open questions

Where the engine takes the 16 palette rows from (the classic .spr palette or a default table: sub_14026E750) was matched by colour, not traced (?).
