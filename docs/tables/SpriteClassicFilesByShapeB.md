# SpriteClassicFilesByShapeB

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140784BE0`
- **Rows:** 170 rows of 8 bytes
- **Keyed by:** sprite shape id
- **Read by:** [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md)
- **Row layout:** [SpriteClassicFileRow](../structs/SpriteClassicFileRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Second copy of the classic sprite file locator table, read when the language code is 0; byte-identical to SpriteClassicFilesByShape.

## Behavior

- V: both copies are read by the same two functions (verified by comparing the bytes: identical).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
