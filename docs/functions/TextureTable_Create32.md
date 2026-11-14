# TextureTable_Create32

- **Address:** `0x1403D1528`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `unsigned int TextureTable_Create32(TextureTable *tbl, int bpp, int w, unsigned int h, const void *pixels)`
- **Callers:** TextureObj_Commit
- **Callees:** sub_14008757C, sub_14003E6D0, sub_14003E7C4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates a w x h 32-bit texture, copies the pixel rows into it and registers it in the global texture table; returns the table index (1..0x7FF) or 0.

## Behavior

- V: finds the first free index i (i = 1.. while tbl[16 + 8 * (i - 1)] != 0; fails when i reaches 0x800). Only bpp == 32 is accepted (else 0).
- V: descriptor {u16 w, u16 h, dword 0x10001, dword 660560, qword 1, dword 0x80000801 (-2147481599)} is passed to sub_14008757C(1, desc, 8) to create the texture; null returns 0. The texture's first mapped surface is obtained with sub_14003E6D0 (the descriptor slot at +0x38 comes back as the row pitch, I), each row (4 * w bytes) is copied with memmove, then sub_14003E7C4 unmaps.
- V: tbl[8 * i + 8] = the texture; returns i.

## Referenced by

- Called by: [TextureObj_Commit](TextureObj_Commit.md)

## Notes

The name is ours (IDB: sub_1403D1528). The slot walk starts at table+16, the store is at table + 8 * i + 8, so index 1 maps to table+16.

## Open questions

? the descriptor constants (format / usage flags) were not decoded.
