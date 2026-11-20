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
- V (data, corrected 2026-11-19): the stock table has 487 rows, keys 0..486; most rows hold the same values (depth bias id 2, camera id 0, scale -1.0 in +20, flags 0 0 1 255) but the rows vary: the camera control key (+0x10) is 1 on key 452 only, own_texture (+0x18) is 1 on 16 rows, +0x19 on 58, +0x1A is 0 on 10, +0x1B is 127 on one, +0x1C is 1 on 17, and one row has colour scale (+8) 0.5 and +0x14 2.0. The camera table has one row, key 1.
- V: the row columns read: +8 colour scale (Effect_TintByNxdScale multiplies the sprite colour bytes by it, 1.0 without a row), +0xC depth bias id, +0x10 camera control key, +0x14 a float that sets two scaled globals (dword_1407DC4F8 and dword_1407DC6C8), +0x18 own_texture (EffectNxd_HasFlag24), +0x19 (read by EffectNxd_HasFlag25, not in this body; stored per texture page, no reader of the stores found), +0x1A and +0x1B copied to renderer slot +92 and +94, +0x1C (read by EffectNxd_HasFlag28, not in this body; changes sprite draw kinds 20 to 21 and 23 to 24).
- V: RefinedVFXCameraControl row: the words at +8, +10 and +12 (columns offset_x, offset_y, offset_z) are added to the first, second and third word of the 21 entries of the tables at +5518.. and +5982.. of the section qword_1411A3860 points to; the byte at +14 sets two words (+5812, +6276) to -1 instead and nothing else of the row is applied; the bytes at +15, +16 and +17 (columns zero_x, zero_y, zero_z) first zero the first, second and third word of the 21 entries of the tables at +5392.. and +5856..; the bytes at +18 and +19 are not read.
- V (2026-11-12): the field it writes at rendererSlot + 88 (g_CharaRenderer + 0x24418 for the effect slot) is written by this function (through rcx + 0x58) and set to -1 at 0x140319FBE (Effect_RunStateMachine) and 0x14031A760 (sub_14031A740); a scan of every instruction for the displacement 0x24418 found no reader (a read through another base register is not excluded: I).

## State touched

- Calls: [NxdEntry_GetRow](NxdEntry_GetRow.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)
- Reads tables: [NxdDataRefinedVFXCameraControl](../tables/NxdDataRefinedVFXCameraControl.md), [NxdDataRefinedVFXTexture](../tables/NxdDataRefinedVFXTexture.md)

## Notes

Name is ours. Because a missing row leaves the renderer fields as the previous effect left them, an effect without a row inherits the last values.

## Open questions

? what the two 21-entry word tables of qword_1411A3860 hold (camera points: I); what the two globals scaled from +0x14 size; what renderer slots +92 and +94, draw kinds 20, 21, 23, 24 and the three page flag globals are used for (readers not found).
