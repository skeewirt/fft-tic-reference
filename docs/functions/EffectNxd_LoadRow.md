# EffectNxd_LoadRow

- **Address:** `0x1400D258C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectNxd_LoadRow(void *rendererSlot, uint32_t effect)`
- **Callers:** sub_140319DA4 (state 3)
- **Callees:** NxdEntry_GetRow, NxdRegistry_Find, NxdTable_GetRowById, sub_1400D2D6C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the Enhanced parameter row of the current effect from the RefinedVFXTexture table (id 202) and applies it to the effect renderer and to the loaded effect data.

## Behavior

- V: stores the effect number at rendererSlot + 88; finds table 202 through NxdRegistry_Find (cached in qword_143CD9F88) and the row whose key equals the effect number; with no table or no row it returns at once and changes nothing else.
- V: from the row it copies two bytes (row +26, +27) into rendererSlot + 92 and + 94, converts the dword at row +12 (the depth bias id) with sub_1400D2D6C into the float at g_CharaRenderer + 147936, and takes the float at row +20 for a scale that sets dword_1407DC4F8 and dword_1407DC6C8.
- V: it then looks up table 317 (RefinedVFXCameraControl, cached in qword_143CD9F80) by the row dword at +16; with no such row it stops. With a row it zeroes or shifts per-slot colour words inside the effect section at qword_1411A3860 (21 entries of 6 bytes at +5394 / +5858 / +5520 / +5984) by the row values.
- V (data): the stock table has 487 rows, keys 0..486, all with the same values (depth bias id 2, camera id 0, scale -1.0 in +20, flags 0 0 1 255); the camera table has one row, key 1.
- V (2026-11-12): the field it writes at rendererSlot + 88 (g_CharaRenderer + 0x24418 for the effect slot) is written by this function (through rcx + 0x58) and set to -1 at 0x140319FBE (Effect_RunStateMachine) and 0x14031A760 (sub_14031A740); a scan of every instruction for the displacement 0x24418 found no reader (a read through another base register is not excluded: I).

## State touched

- Calls: [NxdEntry_GetRow](NxdEntry_GetRow.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)
- Reads tables: [NxdDataRefinedVFXCameraControl](../tables/NxdDataRefinedVFXCameraControl.md), [NxdDataRefinedVFXTexture](../tables/NxdDataRefinedVFXTexture.md)

## Notes

Name is ours. A missing row leaves the renderer fields as the previous effect left them.

## Open questions

? the meaning of the table 202 columns Unknown8, Unknown14 and Unknown18..1C beyond the offsets read here.
