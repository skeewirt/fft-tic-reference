# HdLayer_ResolveQuadTexture

- **Address:** `0x14041AE44`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int HdLayer_ResolveQuadTexture(int *layer, uint16_t *quad, unsigned colour, float w, float h, int *piece)`
- **Callers:** sub_140417690
- **Callees:** sub_14041AC00, HdSheetGroup_FindOrAddPiece, CharaRender_LutUvForQuad, sub_14041E8D4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For a battle HD draw quad, turns its draw id (quad +64) into the HD layer's texture slot and finds or adds the quad's sheet piece in the matching sheet group; then writes the quad's vertices.

## Behavior

- V: with enhanced graphics (g_GraphicsLevel >= 2) and the HD mode dword set, draw id ranges map to HD slot = id - 9992 and a sheet group: 10051..10066 group 0, 10067..10082 group 1, 10083..10098 group 2, 10099..10114 group 3, 10115..10258 group 4 + (id - 10115) / 16 (the nine unit sheets of pools 0..8), 10259..10274 group 13 (pool 9), 10275..10290 group 14, 10339..10354 group 18, 10355..10370 group 19; with refined effect textures on, 10291..10338 groups 15..17.
- V: ids 10000..10050 are a third kind (fixed rectangles), 11111 one special page, 11112..11879 the three face slots (face number through g_FaceG2dEntryByFace, limit 0xCD).
- V: the piece is looked up with HdSheetGroup_FindOrAddPiece(group, rectangle); its index is returned through the last argument.
- V: the highest HD slot any range reaches is 378 (id 10370).

## State touched

- Calls: [HdSheetGroup_FindOrAddPiece](HdSheetGroup_FindOrAddPiece.md), [CharaRender_LutUvForQuad](CharaRender_LutUvForQuad.md)

## Referenced by

- Observed behaviours: [HdLayerUnitSheetsAreTenFixedGroups](../behaviors/HdLayerUnitSheetsAreTenFixedGroups.md)

## Notes

Behavior: HdLayerUnitSheetsAreTenFixedGroups.

## Open questions

None recorded.
