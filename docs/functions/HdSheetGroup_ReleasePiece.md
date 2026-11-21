# HdSheetGroup_ReleasePiece

- **Address:** `0x1403D11DC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void HdSheetGroup_ReleasePiece(void *group, int piece, int free_texture)`
- **Callers:** HdSheetGroup_Reset, HdLayer_BuildTextures
- **Callees:** TextureObj_Reset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Forgets the texture of one piece of a battle HD sheet group; with free_texture also resets the texture object and lowers the group's live count.

## Behavior

- V: on the texture object at group + 2704 + 144 x piece: +112 (key) = -1, +116 (used) = 0, +132 = 0; with free_texture: +120 (age) = 0, TextureObj_Reset, and group +21136 minus one.

## State touched

- Calls: [TextureObj_Reset](TextureObj_Reset.md)

## Referenced by

- Called by: [HdSheetGroup_Reset](HdSheetGroup_Reset.md)

## Open questions

None recorded.
