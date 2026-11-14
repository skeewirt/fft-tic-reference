# g_ErrandActive

- **Kind:** global
- **Address:** `0x1411A71A0`
- **Area:** [Errands](../areas/errands.md)
- **Type:** `uint8[8][9]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The eight active errand slot records, nine bytes each: flags, errand id, town and the three dispatched unit ids.

## Behavior

- V: the errand tick and the errand save copier read and write these slots.

## Referenced by

- Described by tables: [ErrandActive](../tables/ErrandActive.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)
- Read by: [Errand_BuildActiveList](../functions/Errand_BuildActiveList.md), [Errand_Recall](../functions/Errand_Recall.md), [SaveWork_CopyErrandState](../functions/SaveWork_CopyErrandState.md), [sub_1402CCEE0](../functions/sub_1402CCEE0.md)
- Written by: [Errand_Recall](../functions/Errand_Recall.md), [SaveWork_CopyErrandState](../functions/SaveWork_CopyErrandState.md), [sub_1402CCEE0](../functions/sub_1402CCEE0.md)

## Open questions

None recorded.
