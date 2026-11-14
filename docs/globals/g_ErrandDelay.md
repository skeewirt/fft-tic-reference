# g_ErrandDelay

- **Kind:** global
- **Address:** `0x1411A7140`
- **Area:** [Errands](../areas/errands.md)
- **Type:** `uint8[96]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The per-errand delay byte, one per errand id 0..95, saved with the game.

## Behavior

- V: the errand tick reads and writes it; an errand result writes the grade-derived delay.

## Referenced by

- Described by tables: [ErrandDelay](../tables/ErrandDelay.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)
- Read by: [Errand_BuildBoardEntry](../functions/Errand_BuildBoardEntry.md), [Errand_IsOffered](../functions/Errand_IsOffered.md), [Errand_SelectBoardEntry](../functions/Errand_SelectBoardEntry.md), [SaveWork_CopyErrandState](../functions/SaveWork_CopyErrandState.md), [sub_1402CCEE0](../functions/sub_1402CCEE0.md)
- Written by: [SaveWork_CopyErrandState](../functions/SaveWork_CopyErrandState.md), [sub_1402CCEE0](../functions/sub_1402CCEE0.md)

## Open questions

None recorded.
