# PreviewUnit_ResolveShape

- **Address:** `0x1400FCAB0`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void PreviewUnit_ResolveShape(unsigned idx, char *outShape, uint8_t *outPalette)`
- **Callers:** sub_1400FB038, sub_14022AA88, sub_1402C1D40
- **Callees:** Unit_ResolvePreviewShape, sub_140260ABC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves shape/palette for entry `idx` (<= 0x14) of the 21-entry preview table g_BattleUnitTable (stride 512).

## Behavior

- V: calls Unit_ResolvePreviewShape; stores shape at entry+399 and palette at +400; the palette may be overridden by a table lookup (sub_140260ABC).

## State touched

- Calls: [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md)

## Referenced by

- Called by: [PreviewUnit_BuildSpriteRecord](PreviewUnit_BuildSpriteRecord.md), [Unit_BuildPreviewSpriteRecord](Unit_BuildPreviewSpriteRecord.md), [sub_14022AA88](sub_14022AA88.md)

## Notes

Bound check `idx <= 0x14` already admits index 20.

## Open questions

Live table reads as zeros when the tree is open; is it only populated in battle/party contexts? Not investigated.
