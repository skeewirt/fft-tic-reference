# HdSheetAndClassicPaletteLoading

- **Kind:** observed behaviour
- **Scope:** engine (sprite sheets and palettes)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [sub_1403D2450](../functions/sub_1403D2450.md), [PackFile_ReadEntry](../functions/PackFile_ReadEntry.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a sprite number becomes a sheet and a palette: a g2d entry pair through the HD table and the pack's unchecked index table, and a palette from the classic file named in the classic table.

## Behavior

- V: CharaRender_BuildAtlasTexture reads the entry from the HD table (no sheet above 0xA9; -1 for sprites 155 to 158 means entry 160 with a palette from file kind 72), then loads entry and entry + 1 through sub_1403D2450, PackFile_ReadEntry and sub_1403D25A4 from the pack handle qword_140D3AD58.
- V: sub_1403D2450 and PackFile_EntryPtr index the pack's 16-byte offset rows with the entry number and no bound check.
- V: the palette comes from CharaPalette_LoadClassic (first 0x200 bytes of the classic file, then the CharShape colour override); the sheet's pixels are 4-bit indexes into it, so the colours follow the classic file.
- V: CharaPalette_LoadClassic has no bound on the sprite number; it reads the pair at table + 8 * sprite.

## Open questions

None recorded.
