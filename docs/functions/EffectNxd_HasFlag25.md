# EffectNxd_HasFlag25

- **Address:** `0x1400D2B4C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool EffectNxd_HasFlag25(int effect)`
- **Callers:** sub_1400D2C74
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reports whether the RefinedVFXTexture row of an effect has its byte at +25 set.

## Behavior

- V: false for an effect of 0 or less, for a missing table or a missing row; otherwise the byte at row +25 is non-zero.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [EffectNxd_SelectPageTexture](EffectNxd_SelectPageTexture.md)
- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)
- Reads tables: [NxdDataRefinedVFXTexture](../tables/NxdDataRefinedVFXTexture.md)

## Notes

Name is ours. The column is Unknown19 in the table layout.

## Open questions

? what the flag selects.
