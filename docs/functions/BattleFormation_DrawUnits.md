# BattleFormation_DrawUnits

- **Address:** `0x140216EB4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void BattleFormation_DrawUnits(void *a1)`
- **Callers:** sub_140213F14
- **Callees:** SceneObject_FindByUnitIndex, NxdRegistry_Find, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle formation draw (called from sub_140213F14): per unit index 0..20 it reads the CharShape row of the scene object's sprite byte for the draw height.

## Behavior

- V: the key is the scene object's byte +0xA (0x14021708E); table 174 (CharShape) through NxdRegistry_Find (cached in `qword_143CD9F38`), entry = NxdTable_GetRowById(table, key); an entry with a negative first qword gives the static default row (`unk_1406F5ED0`), else NxdEntry_GetRow(entry).
- V: a null entry gives a null row and the function reads row +0x2F (0x14021714B, when scene object +0x15C bit 2 is set) and row +0x2C (0x140217172) through it with no test: an access violation that ends the thread (seen live 2026-11-13 on a resumed battle whose units carried shape bytes with no CharShape row).
- V: other scene object fields read: +0x1E a byte the formation scales by 12; +0x15C bit 2 selects the +0x2F test.

## State touched

- Calls: [SceneObject_FindByUnitIndex](SceneObject_FindByUnitIndex.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Reads tables: [NxdDataCharShape](../tables/NxdDataCharShape.md)

## Notes

Behavior: CharShapeRowMissingFaultsTheFormation.

## Open questions

None recorded.
