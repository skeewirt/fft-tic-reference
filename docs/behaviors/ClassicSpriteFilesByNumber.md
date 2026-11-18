# ClassicSpriteFilesByNumber

- **Kind:** observed behaviour
- **Scope:** the sprite pack, classic palettes and portraits of stock shapes
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [GameData_ReadSectors](../functions/GameData_ReadSectors.md), [PackFile_ReadEntry](../functions/PackFile_ReadEntry.md), [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Classic sprite files are numbered entries of fftpack.bin, and the `offset` column of the classic kind tables is that file number; the game has no portrait for shapes 56 and 57.

## Behavior

- V (data): `system/ffto/fftpack.bin` (the English pack `fftpack.en.bin`, 213,143,552 bytes inflated) has header dwords 3931 (file count), 16, 15740, 32768, then 3931 byte offsets and 3931 sizes (offsets in bytes, not sectors). The game's pack 0002 also holds named copies of 178 `fftpack/unit/*.bin` files; each tested named copy is byte-identical to exactly one fftpack entry: `battle_dami_spr.bin` = file 91 (44,690 bytes), `battle_kasanek_spr.bin` = 130 (40,516), `battle_mina_m_spr.bin` = 140 (43,433; the Squire's, found by pixels).
- V (data): the `offset` column of `exe.sprite.classic_kind` / `classic_kind2` is this file number (the first argument of GameData_ReadSectors); stock shapes 93 and 94 use files 91 and 130, shape 56 uses 152, shape 57 uses 140, both through both tables.
- V (data): `exe.sprite.hd_entry_by_shape`: shape 56 -> g2d entry 922, shape 57 -> 924 (each shape's second sheet is the next entry); shapes 159..169 -> 1110, 1112 .. 1130.
- V (data): the game's packs hold no `wldface_056_*` or `wldface_057_*` portrait; `wldface_058_08` exists. The four portrait code tables hold 0 for shapes 55, 56, 57, 93, 94; `exe.sprite.scene_shape` (sprite id 0..159 -> shape) maps no id to shape 56 or 57 (id 141 -> 58). I: so no portrait code gives a unit of look 56 / 57 the face 56 / 57 through the stock path.
- V (seen live 2026-11-14): a party unit's save record (`g_UnitSaveData` + 600 n, byte +0) set to a value below 0x80 makes the roster draw that look: look 56 showed the art of g2d entry 922 with the colours of classic file 152, and Ramza's portrait (code 0).
- V (data): a classic sprite file's 4-bpp pixels (after its 0x200-byte palette, 256 pixels a row) and its HD sheet (512 a row) share colour indices at double size: sampled every 3 pixels, a sheet and its own classic file agree on 73 % and 76 % of the classic file's non-transparent pixels (the two test pairs), unrelated pairs on 2 % to 13 %.
- V (data): the pack index of the game's packs records a CRC and a size per file (`fftpack.en.bin`: size 0x0CB45000, the uncompressed size), readable without inflating the file.
- V (seen live 2026-11-14): the face number is formatted into the texture name unchanged at four digits: a face number 9056 resolved to `wldface_9056_08`.

## Open questions

None recorded.
