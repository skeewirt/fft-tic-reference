# HdSheetGroup

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 21144 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One of the 20 sheet groups of the battle HD layer (g_HdSheetGroups): a sheet entry kept in memory and the textures cut from it, one per piece and palette.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="index"></a>`0x0` | index | `int32` | V | The group's own number (HdLayer_BuildTextures writes it before it uses the group). |
| <a id="pieces"></a>`0x4` | pieces | `int32[134][5]` | I | Rectangles of the sheet's pieces, 20 bytes each (x, y, width, height first): a draw record names one by its dword +72. I: the count follows from the space up to +2692. |
| <a id="entry"></a>`0xA84` | entry | `int32` | V | The g2d entry the buffer holds; a draw record with another entry frees the group's textures and reads the new one. |
| <a id="pixels"></a>`0xA88` | pixels | `pointer` | V | The entry's bytes (0x80000 bytes, allocated once and zeroed). |
| <a id="textures"></a>`0xA90` | textures | `record[128]` | V | 144 bytes each: a texture object, then at +112 the palette hash, +116 in use, +120 the age (60 when used, counted down), +124..+136 the piece's x, y, width, height. |
| <a id="count"></a>`0x5290` | count | `int32` | V | Number of textures made in the group. |

## Behavior

- V: groups 15 to 17 are built with 256 palette colours and 8-bit pixels, every other group with 16 colours and 4-bit pixels (HdLayer_BuildTextures passes the pixel width to HdGroup_BuildPiece).

## Referenced by

- Observed behaviours: [SixteenColourLimitIsTwoCpuBuilders](../behaviors/SixteenColourLimitIsTwoCpuBuilders.md)

## Notes

The names are ours.

## Open questions

None recorded.
