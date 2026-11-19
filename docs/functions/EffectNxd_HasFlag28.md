# EffectNxd_HasFlag28

- **Address:** `0x1400D2BE0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool EffectNxd_HasFlag28(int effect)`
- **Callers:** sub_1400D2D30
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reports whether the RefinedVFXTexture row of an effect has its byte at +28 set.

## Behavior

- V: false for an effect of 0 or less, for a missing table or a missing row; otherwise the byte at row +28 is non-zero.
- V: sub_1400D2D30 uses it to swap a model type of 20 for 21 and 23 for 24.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [EffectNxd_AdjustSpriteKind](EffectNxd_AdjustSpriteKind.md)
- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)
- Reads tables: [NxdDataRefinedVFXTexture](../tables/NxdDataRefinedVFXTexture.md)

## Notes

Name is ours. The column is Unknown1C in the table layout.

## Open questions

None recorded.
