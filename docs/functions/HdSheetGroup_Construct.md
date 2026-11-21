# HdSheetGroup_Construct

- **Address:** `0x1403D0D4C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void *HdSheetGroup_Construct(void *group)`
- **Callers:** HdSheetGroups_ConstructAll
- **Callees:** sub_1403D0898

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds one battle HD sheet group: its 128 texture objects, an empty piece list, 16 free palette entries and no sheet.

## Behavior

- V: the layout (0x5298 bytes): +0 the group number (-1 until first use); +4 128 pieces of 20 bytes (rectangle x, y, w, h and a used dword); +2564 16 palette entries of 8 bytes (CLUT word, used flag); +2692 the sheet entry loaded into the buffer (-1 = none); +2696 the 0x80000-byte sheet buffer (allocated on first use by HdLayer_BuildTextures); +2704 128 texture objects of 144 bytes (one per piece: +48 the texture id written into draw records, +112 a key, -1 = none, +116 the used-this-frame flag, +120 the age counter that HdLayer_BuildTextures sets to 60 on use and counts down); +21136 the count of live textures.
- V: each texture object is set up by sub_1403D0898; the pieces, palette words and sheet entry are set empty.

## State touched

- Calls: [sub_1403D0898](sub_1403D0898.md)

## Referenced by

- Called by: [HdSheetGroups_ConstructAll](HdSheetGroups_ConstructAll.md)
- Observed behaviours: [WordSeventeensArithmeticReachesNewSheetGroups](../behaviors/WordSeventeensArithmeticReachesNewSheetGroups.md)

## Open questions

None recorded.
