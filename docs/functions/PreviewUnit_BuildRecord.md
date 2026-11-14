# PreviewUnit_BuildRecord

- **Address:** `0x1400FB164`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 PreviewUnit_BuildRecord(SpriteRecord *out, int partyIndex, int previewIndex, int a4, int a5, int slotArg, char applyAltRow)`
- **Callers:** Unit_BuildPreviewSpriteRecord (when unk_142FF9F30 and qword_142FF9F34 are both 0, i.e. always in normal play), sub_140143EA8, sub_140147268, sub_140218F78, sub_1402D0108, sub_1402D3838, sub_1402ED078
- **Callees:** Unit_ResolvePreviewShape, SpriteRecord_Fill, UITable_GetRowByKey, sub_1401E39BC, sub_140275C70

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Normal-play builder of a unit's sprite record: creates the preview unit, resolves its shape and palette, fills the record and applies the alternate row (table 0x112).

## Behavior

- V: builds a 512-byte preview unit with sub_140275C70(previewIndex), calls Unit_ResolvePreviewShape (shape, palette); for a unit with flag 4 it takes the palette from the save data byte +288 (+0x120).
- V: calls SpriteRecord_Fill(out, partyIndex, shape, palette, a4, 0, slotArg, flagWord) where flagWord = 0x40000000 when the unit's low nibble (byte +8 of the preview unit; the 'flag 4' test is bit 4 of byte +6) is <= 1, else 0x20000000, only for a unit with flag 4 and save data, otherwise 0; slotArg is the caller's 2 * slot + 4.
- V: with applyAltRow, row 0x112 (by the unit's first byte) sets record +10 from sub_1401E39BC when its field +4 is non-zero.
- V: the byte answer of Unit_ResolvePreviewShape is zero-extended into r11d at 0x1400FB1D4, copied to the work record's +399 (0x1400FB1D8) and handed to SpriteRecord_Fill as r8d (0x1400FB23F).

## State touched

- Calls: [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md), [SpriteRecord_Fill](SpriteRecord_Fill.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [Errand_BuildBoard](Errand_BuildBoard.md), [SaveHeader_FillBattleFields](SaveHeader_FillBattleFields.md), [SaveWork_PackFromLive](SaveWork_PackFromLive.md), [Unit_BuildPreviewSpriteRecord](Unit_BuildPreviewSpriteRecord.md)
- Observed behaviours: [JobTreePanelSprite](../behaviors/JobTreePanelSprite.md)

## Notes

Supersedes the impression that PreviewUnit_BuildSpriteRecord is the tree's builder: that one is only reached when the two debug globals are set.

## Open questions

None recorded.
