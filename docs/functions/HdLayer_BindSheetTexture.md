# HdLayer_BindSheetTexture

- **Address:** `0x14041D670`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char HdLayer_BindSheetTexture(int *a1, unsigned a2, unsigned a3, __int64 a4, unsigned a5, unsigned a6, char a7)`
- **Callers:** sub_140417690
- **Callees:** sub_1400D29F0, sub_14041E864

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds a sprite sheet texture id of the battle HD layer to the g2d entry that the sheet slot table holds.

## Behavior

- V: for ids 123 to 266 the entry is dword_142E7FEBC[(id - 123) / 16], for 267 to 282 dword_142E7FEE0[(id - 267) / 16], for 283 to 298 dword_142E7FEE4, and fixed slots hold the other ids; the entry is stored in the draw record at +64.
- V: the first three ids use the face table at 0x140714EA0 (limit 0xCD) instead.
- V (2026-11-20): the full map: 59..74 slot 16, 75..90 slot 17, 91..106 slot 18, 107..122 slot 19, 123..266 slots 20..28 (pools 0..8), 267..282 slot 29 (pool 9), 283..298 slot 30, 299..346 slots 31..33 (sub_1400D29F0, effect pages), 347..362 slot 34, 363..378 slot 35; the HD layer's texture tables end at 378 (HdLayer_BuildTextures).
- V: binds the HD texture ids of the pool sheets (123 + 16 p + frame) to the g2d entry `dword_142E7FEBC[p]` (= g_HdSheetEntryBySlot[20 + p]); HdLayer_BuildTextures loads an entry that differs from the slot's loaded one with PackFile_ReadEntry(g2d pack `qword_140D3AD58`, entry).

## State touched

- Reads: [g_FaceG2dEntryByFace](../globals/g_FaceG2dEntryByFace.md)

## Referenced by

- Observed behaviours: [FaceNumberCapsClipRawCodesToo](../behaviors/FaceNumberCapsClipRawCodesToo.md), [HdLayerUnitSheetsAreTenFixedGroups](../behaviors/HdLayerUnitSheetsAreTenFixedGroups.md), [HdSheetFromSlotColoursFromRecord](../behaviors/HdSheetFromSlotColoursFromRecord.md)

## Notes

The slot dwords are the ones SceneUnit_BuildFromQueueEntry and sub_140260CF0 fill; there are 9 unit slots plus the shared slot 17.

The face table at 0x140714EA0 (206 g2d entry numbers) has four readers, each comparing the slot value unsigned with 0xCD first: sub_14041AE44 (0x14041B34E), sub_14041CAAC (0x14041CC09), this function (0x14041DA3F) and sub_14041DAA4 (0x14041DB82) (V, xrefs). Corrected 2026-11-08: this sheet named only one.

## Open questions

? the role of the 152-byte draw record.
