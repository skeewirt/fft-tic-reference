# HdSheetGroup_FindOrAddPiece

- **Address:** `0x1403D0EF0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int HdSheetGroup_FindOrAddPiece(void *group, const int rect[4])`
- **Callers:** HdLayer_ResolveQuadTexture
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a sheet piece (a 4-dword rectangle) among the 128 piece entries of an HD sheet group, or stores it in the first free entry; returns the entry index (0 when the group is full).

## Behavior

- V: entries are 20 bytes from group +4: the 4 rectangle dwords and a used dword; a match sets the used dword and returns its index; else the first entry whose used dword is 0 takes the rectangle.

## Referenced by

- Called by: [HdLayer_ResolveQuadTexture](HdLayer_ResolveQuadTexture.md)
- Observed behaviours: [HdLayerUnitSheetsAreTenFixedGroups](../behaviors/HdLayerUnitSheetsAreTenFixedGroups.md)

## Open questions

None recorded.
