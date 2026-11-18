# CharClut_ApplyToPalette

- **Address:** `0x14026C530`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void CharClut_ApplyToPalette(uint32_t clutId, uint16_t *pal)`
- **Callers:** CharShape_ApplyClut, CharaRender_BuildAtlasTexture
- **Callees:** `sub_1403D325C` (table by id), `sub_1403D3AE8`, `sub_1403D3A34` (row count), `sub_1403D3C98` (row by index), `sub_1403D2FD8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the CharCLUT rows of one key to a palette: each enabled row replaces one 16-colour block with colours given as 8-bit RGB triples.

## Behavior

- V: fetches the CharCLUT table (id 210) lazily and loops over all rows whose key is clutId.
- V: a row is used only when its flag byte at +20 is non-zero.
- V: for an enabled row it reads a block index from the row's sub-record (second pointer, dword at +4) and writes 16 colours starting at palette entry 16 x block index.
- V: each colour comes from 3 bytes (R, G, B); the top 5 bits of each channel are packed with red in the low bits, green in the middle and blue on top, giving a 15-bit value.
- V: bit 15 is set on every colour of the block except the first, mirroring the loader's rule that colour 0 carries no opaque bit.
- I: the block-index source (the sub-record dword) was read from the decompilation but its table column was not named.

## Referenced by

- Called by: [CharShape_ApplyClut](CharShape_ApplyClut.md)
- Reads tables: [NxdDataCharCLUT](../tables/NxdDataCharCLUT.md)

## Notes

This is the hook through which a data row can recolour a shape without a new sprite file.

## Open questions

None recorded.
