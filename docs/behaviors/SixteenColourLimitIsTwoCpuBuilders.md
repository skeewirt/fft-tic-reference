# SixteenColourLimitIsTwoCpuBuilders

- **Kind:** observed behaviour
- **Scope:** engine (unit sheets)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [HdLayer_BuildTextures](../functions/HdLayer_BuildTextures.md), [HdGroup_BuildPiece](../functions/HdGroup_BuildPiece.md), [Pixels_ExpandToRgba](../functions/Pixels_ExpandToRgba.md), [Rgb555ToRgba8888](../functions/Rgb555ToRgba8888.md), [HdSheetGroup](../structs/HdSheetGroup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 15 colours of a unit sheet (16 with the transparent one) are a property of two CPU routines that expand 4-bit pixels through 16 converted colours; both hand the GPU 32-bit textures, and the battle one already has an 8-bit, 256-colour branch.

## Behavior

- V: menus: CharaRender_BuildAtlasTexture reads the sheet entry, converts 16 colours and writes a 512 x 512 buffer of 32-bit texels for TextureObj_SetSource.
- V: battle: HdLayer_BuildTextures reads the entry into a sheet group and HdGroup_BuildPiece expands a piece through the converted colours into 32-bit texels; its pixel width argument is 4 or 8.
- V: the game itself uses the 8-bit branch with 256 colours for the sheet groups 15 to 17.
- V: the HD sheet entries are 512 pixels wide at 4 bits (131072 bytes for 512 rows, 118784 for 464); the buffers they are read into hold 0x100000 bytes (menus) and 0x80000 bytes (a sheet group), so an 8-bit entry of the same size in pixels (262144 and 237568 bytes) fits both.

## Open questions

None recorded.
