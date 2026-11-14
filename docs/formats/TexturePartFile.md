# TexturePartFile

- **Kind:** file format
- **Extension:** `.utexpt`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Read by:** [GUIFontSlotGroup_OnPartTableLoaded](../functions/GUIFontSlotGroup_OnPartTableLoaded.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The part file that names the texture a UI image part shows (ui/ffto/icon/<kind>/textureparts/<name>.utexpt).

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="path_offset"></a>+0 | path_offset | `uint32` | V | 0x20: where the texture path starts. |
| <a id="type_name_size"></a>+4 | type_name_size | `uint32` | I | 12: the length of 'TexturePart' with its terminator. |
| <a id="part_count"></a>+8 | part_count | `uint32` | I | 1. |
| <a id="type_name_offset"></a>+12 | type_name_offset | `uint32` | I | Offset of the type name from this field: 0x20 + path length (with terminator) - 12. |
| <a id="reserved"></a>+16 | reserved | `uint32[2]` | ? | Zero in every file read. |
| <a id="size"></a>+24 | size | `uint32[2]` | I | 0x30, 0x30: the icon area (48 x 48) of a 60 x 60 job icon texture. |
| <a id="texture_path"></a>+32 | texture_path | `char[]` | V | Terminated path of the texture, e.g. the job icon texture of that index. |
| <a id="type_name"></a>after the path | type_name | `char[]` | V | 'TexturePart', terminated. |

## Behavior

- V: a file built from this layout equals the retail job icon part files j_020 and j_003 byte for byte.

## Notes

V (header of the stock ei_001 part file): the dword at +0 is 0x20 and the texture path starts at +0x20. V: the dword at +0x0C is the offset of the part-name string relative to +0x0C: 0x44 in ei_001, so the string starts at 0x50; 0x48 in ei_s_123, whose longer equip_item_s path pushes the name four bytes further. V: both files hold one part (count 1 at +0x08), are 0x5C and 0x60 bytes long, and name the literal TexturePart. V: the same header values repeat across the six ei_000..ei_005 files and the four ei_s_120..ei_s_123 files read.

## Open questions

? Whether the game loads a part file that no retail pack has.
