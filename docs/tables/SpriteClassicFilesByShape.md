# SpriteClassicFilesByShape

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140784690`
- **Rows:** 170 rows of 8 bytes
- **Keyed by:** sprite shape id
- **Read by:** [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md)
- **Row layout:** [SpriteClassicFileRow](../structs/SpriteClassicFileRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Classic sprite file locator per shape, used for the palette load of the HD sheet. CharaPalette_LoadClassic reads this copy when the language code is not 0 and SpriteClassicFilesByShapeB when it is 0; the two copies are byte-identical.

## Behavior

- V: the language code is the dword at +8 of the language info record (1 when there is none).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: why the game keeps two identical copies
