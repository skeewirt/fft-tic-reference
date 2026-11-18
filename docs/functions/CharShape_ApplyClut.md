# CharShape_ApplyClut

- **Address:** `0x14026C7AC`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void CharShape_ApplyClut(uint8_t shape, uint16_t *pal)`
- **Callers:** CharaPalette_LoadClassic, sub_14026E838
- **Callees:** CharClut_ApplyToPalette, `sub_1403D3AE8` (row by key), `sub_1403D2FD8` (row data pointer)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up the shape's row in the CharShape table and, if the row names a colour-override set, applies it to the palette.

## Behavior

- V: fetches the CharShape table (id 174) lazily from the table registry and the row whose key is the shape.
- V: reads the row's dword at +12 (the colour-override key, column `charclut+Id`); if it is non-zero it calls CharClut_ApplyToPalette(clutId, pal).
- V: a missing table, missing row or a zero key leaves the palette unchanged.
- V: called by CharaPalette_LoadClassic and by one other palette loader (sub_14026E838, the battle side).
- V: the key is narrowed to its low byte (zero-extending byte load at 0x14026C7C0) before NxdTable_GetRowById, which itself takes a 32-bit key; the two callers hand only a byte register: CharaPalette_LoadClassic the low byte of the 32-bit look at 0x14026E806, sub_14026E838 the scene unit's sprite byte (+0xA) at 0x14026E8F3.

## State touched

- Calls: [CharClut_ApplyToPalette](CharClut_ApplyToPalette.md)

## Referenced by

- Called by: [CharaPalette_LoadClassic](CharaPalette_LoadClassic.md), [sub_14026E838](sub_14026E838.md)
- Observed behaviours: [CharShapeKeyByteSites](../behaviors/CharShapeKeyByteSites.md), [CharShapeRowMissingFaultsTheFormation](../behaviors/CharShapeRowMissingFaultsTheFormation.md), [CharShapeRowsANewLookNeeds](../behaviors/CharShapeRowsANewLookNeeds.md), [SpriteNumberStoreWidths](../behaviors/SpriteNumberStoreWidths.md)
- Reads tables: [NxdDataCharShape](../tables/NxdDataCharShape.md)

## Notes

Every generic job shape has override key 0, so the classic file's own palette is used unchanged for them.

## Open questions

None recorded.
