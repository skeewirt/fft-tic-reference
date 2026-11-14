# SpriteNumberStoreWidths

- **Kind:** observed behaviour
- **Scope:** engine (unit sprite number)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_ResolvePreviewShape](../functions/Unit_ResolvePreviewShape.md), [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [CharShape_ApplyClut](../functions/CharShape_ApplyClut.md), [UnitWork_ApplyJobRow](../functions/UnitWork_ApplyJobRow.md), [SpriteRecord_Fill](../functions/SpriteRecord_Fill.md), [CharaRender_SetSlotRequest](../functions/CharaRender_SetSlotRequest.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which stores of a unit's sprite number are bytes and which are wider: the battle path keeps the number in bytes (limit 255) while the menu path carries it as a 32-bit value.

## Behavior

- V: byte stores: the return value of Unit_ResolvePreviewShape, the unit field +0x18F and +0x190, the scene-unit field +0xA, both leading bytes of a look pool record, the argument of CharShape_ApplyClut, the job row bytes +46 (own sprite number) and +47 (palette byte), the roster record marker.
- V: a roster record's first byte below 0x80 is the sprite number itself; 0x80 and 0x81 mean 'generic man or woman' (look from the job byte), 0x82 'own look from the job row', 0xA2, 0xA3, 0xA5 and 0xA6 to 0xA9 fixed looks, other values the job id plus 40.
- V: the load queue holds the sprite as a 16-bit word but LookQueue_Add replaces a signed value of 170 or more by 1 (the cmp is signed, so values above 32767 also pass as non-negative).
- V: the menu sprite record keeps the sprite as a 32-bit value at +4 and the renderer slot cache as a 32-bit value; CharaRender_BuildAtlasTexture compares it unsigned with 0xA9 and the attribute reads in CharaRender_SetSlotRequest use its low 16 bits.
- V: UnitWork_ApplyJobRow copies job row +46 and +47 to unit +0x18F and +0x190; that is the one data-driven sprite number the game has (a unit with marker 0x82 draws it).

## Open questions

? the readers of unit +0x18F in sub_1402ADA84 and the 40 other direct reads were not each opened.
