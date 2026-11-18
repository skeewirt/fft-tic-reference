# CharaRender_LookupLutParams

- **Address:** `0x1400CBFD0`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 CharaRender_LookupLutParams(__int64 table, unsigned shape, LutCfg *out)`
- **Callers:** CharaRender_DrawFrame, sub_14027032C
- **Callees:** sub_1403D325C (table by id), sub_1403D3AE8 (row by key), sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up the per-shape rows that drive a unit's shadow size and LUT region: shape row -> shadow-size row and LUT-parameter row.

## Behavior

- V: shape row (nxd table id 174, I: CharShape; columns at row +8 shadowsize Id1, +12 CLUT id, +16 lutparam Id1, +20 shadowsize Id2, +24 lutparam Id2, +28 lutparam Id3, +32 lutparam Id4).
- V: with cfg byte 0 = 0 it uses shadowsize Id1 (+8) and lutparam Id1 (+16); with cfg byte 0 set, Id2 (+20 / +24); with cfg byte 2 set and byte 1 clear, lutparam Id3 (+28, byte 2 < 2) or Id4 (+32).
- V: shadow size row (I: CharShapeShadowSize, id 176) +8 -> cfg +4; LUT parameter row (I: CharShapeLUTParam, id 217) +8 / +12 floats -> cfg +8 / +12, +16 / +18 shorts -> cfg +16 / +18; shape row bytes +45 / +46 -> cfg +3 / +20.

## Referenced by

- Called by: [CharaRender_DrawFrame](CharaRender_DrawFrame.md)
- Observed behaviours: [CharShapeRowsANewLookNeeds](../behaviors/CharShapeRowsANewLookNeeds.md)
- Reads tables: [NxdDataCharShape](../tables/NxdDataCharShape.md), [NxdDataCharShapeLUTParam](../tables/NxdDataCharShapeLUTParam.md), [NxdDataCharShapeShadowSize](../tables/NxdDataCharShapeShadowSize.md)

## Notes

Column order matches the CharShape table of the studio's base database (tic_base.sqlite); every generic job shape (96..133) has lutparam Id1 = 2 -> CharShapeLUTParam row 2 = (0.375, 0.45, 0, -6).

## Open questions

Table id to name links are inferred from row layouts (I).
