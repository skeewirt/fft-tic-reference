# g_AbilityMpCost

- **Kind:** global
- **Address:** `0x1407B078E`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The MP cost of the action being started or previewed: the action row's cost byte, halved for a unit with the halving passive; zero when no cost applies.

## Behavior

- V: sub_1402828E4 clears it and writes it (0x140282918, 0x1402829BC) and sub_14030B1A0 clears it and writes it (0x14030B1C9, 0x14030B265).
- V: sub_14030B4F0 (0x14030B8C2, 0x14030B8D8, 0x14030B945) and sub_14030BEB4 (0x14030BEB8, 0x14030BEF3) read it.
- V: an ability above 0x16F never reaches the write, so the byte stays zero for it; see AbilityAboveStockBoundaryHasNoMpCheckOrCost.

## Referenced by

- Observed behaviours: [AbilityAboveStockBoundaryHasNoMpCheckOrCost](../behaviors/AbilityAboveStockBoundaryHasNoMpCheckOrCost.md)
- Written by: [sub_1402828E4](../functions/sub_1402828E4.md), [sub_14030B1A0](../functions/sub_14030B1A0.md)

## Open questions

? what sub_14030B4F0 and sub_14030BEB4 show or do with the cost.
