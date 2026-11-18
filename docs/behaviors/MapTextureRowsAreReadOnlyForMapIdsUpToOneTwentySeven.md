# MapTextureRowsAreReadOnlyForMapIdsUpToOneTwentySeven

- **Kind:** observed behaviour
- **Scope:** engine (map texture set)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapTextures_LoadMapSlots](../functions/MapTextures_LoadMapSlots.md), [MapTextures_LoadSystemSlots](../functions/MapTextures_LoadSystemSlots.md), [MapTextures_NameOfFrame](../functions/MapTextures_NameOfFrame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The loader of the map's colour and lighting textures reads the RefinedBgTexture rows only when the map id is 127 or less; for a larger id it requests no map texture at all. The system textures have no such bound.

## Behavior

- V: the id field of the texture set is compared unsigned with 0x7F before the table is touched; above it the slot count is 0.
- V: the same loader also needs the texture-source field to be 0; that field's writer was not found (?).
- V: MapTextures_LoadSystemSlots has no id compare: no row, or an empty name, requests the stock default colour table file.
- V: other id compares on the path: MapMesh_StockNodeOffset returns at once above 116; MapMesh_Load skips 15 and 33.
- V: census of the compares of the map id with 127, 128 or 255 over the renderer functions and every function that reads the three map-id globals: the texture loader's compare above is the only range test; the palette command in MapBlock_RunCommand tests map 127 for equality (a fixed branch, every other id takes the default); the other 7Fh and FFh immediates in those functions mask or test unit and node data, not the id.
- V: the id is stored as a byte in the save header (the low byte of the battle map id), so 255 is the largest id the header can show; the id field of the texture set is a 32-bit copy of the loader's id, which is a 16-bit argument: ids 256 to 65535 are the only values above 255 that can reach the compare.

## Notes

Stock rows of the renderer tables end at id 116; ids 117..128 have no row and no mesh file.

## Open questions

None recorded.
