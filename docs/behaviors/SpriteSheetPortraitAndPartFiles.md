# SpriteSheetPortraitAndPartFiles

- **Kind:** observed behaviour
- **Scope:** engine (sprite sheet, classic file and portrait files)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_1403D2450](../functions/sub_1403D2450.md), [PackFile_ReadEntry](../functions/PackFile_ReadEntry.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md), [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [FaceTexture_FormatName](../functions/FaceTexture_FormatName.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A unit sprite is two HD sheet entries plus a classic file whose first 0x200 bytes are its palettes; a portrait is a texture plus a part file that the game asks for by name.

## Behavior

- V: an HD sheet is the pair of g2d.dat entries named by SpriteHdEntryByShape row L and the next; the game loads each with sub_1403D2450(g2d, n, n + 1) and PackFile_ReadEntry(g2d, n, out), which inflates it (a 16-byte YOX block header, then zlib). A generic job's pair is 131072 + 118784 bytes inflated (512 x 512 and 512 x 464, 4 bpp).
- V: the palette the sheet is drawn with is the first 0x200 bytes (16 palettes of 16 BGR555 colours) of the classic sprite file named by SpriteClassicFilesByShape row L (file number, size), read by GameData_ReadSectors.
- V: a portrait is ui/ffto/common/face/texture/wldface_<F>_<c>_uitx.tex plus the part file textureparts/wldface_<F>_<c>_uitx.utexpt that names it.
- V (live 2026-11-10): an HD sheet is the classic 256 x 488 sheet at twice the size in both directions, rows 0..255 in the first entry and 256..487 in the second, 4 bpp with the left pixel in the low nibble: a PlayStation-format sprite with every pixel doubled drew correctly.
- V (the part file of a stock portrait, read 2026-11-19): a portrait texture is 520 x 388 and its part file names eight parts of 128 x 192: Eye00 (1, 1), Eye01 (131, 1), Eye02 (261, 1), Mouth00 (1, 195), Mouth01 (131, 195), Mouth02 (261, 195), Mouth03 (391, 195) and All (391, 1).
- M (one stock portrait, face 096): the eye parts are drawn only in their rows 0..125 (the head down to the eyes: open, half shut, shut), the mouth parts only in their rows 117..192 (the chin and bust with four mouth shapes), All holds the whole picture; the ground around the figure is clear (20 % of All), the edges are softened (alpha steps, 260 colours in All).
- M (2026-11-19, the 108 humanoid sheets, the 288 plain rows of each classic file against the same rows of the HD sheet): every HD sheet lies exactly over its classic sheet at twice the size (no sheet matches better moved by a pixel) and uses the same colour slots, but it is not the classic sheet with its pixels doubled: 59.7 % of the drawn pixels equal the doubled classic pixel (39.7 % to 67.1 % by sheet), 44 % of the 2 x 2 blocks are one colour, in 21 % of the blocks the classic pixel's colour does not appear at all, about 12 % of the doubled drawn area is empty in the HD sheet and 9 % of the HD drawn area is empty in the doubled one.
- M (same pairs): 79.4 % of the drawn HD pixels have a colour of the 3 x 3 classic neighbourhood they lie in; the classic edge rule Scale2x reproduces 63.0 % of them.
- V (format of a .utexpt part file, stock icon and face files): +0 the texture path's offset P, +8 the part count n, n records of 20 bytes from +0x0C (name offset relative to the record, x0, y0, x1, y1; record 0 is the whole texture), P = 0x0C + 20 n, then the NUL-terminated path and the part names.

## Notes

Not yet seen: a sheet of another size, the classic graphics mode.

## Open questions

? what else reads a classic file (classic graphics mode draws the classic sheet itself); ? whether any reader bounds a g2d entry number.
