# Errand_IsOffered

- **Address:** `0x1402EE0A4`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `bool Errand_IsOffered(int errand, int town)`
- **Callers:** sub_1402EDF94, sub_140344B68, sub_14036E5DC
- **Callees:** EventVar_Read, Errand_IsAvailable

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Whether an errand is offered at a town now: not dispatched, not completed, no delay left, and available there.

## Behavior

- V: false when EventVar_Read(864 + errand) has 0x02 or 0x04, or when the low 6 bits of g_ErrandDelay[errand] are not 0.
- V: otherwise the answer of Errand_IsAvailable(errand, town + 1).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [Errand_IsAvailable](Errand_IsAvailable.md)
- Reads: [g_ErrandDelay](../globals/g_ErrandDelay.md)

## Referenced by

- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Notes

Name is ours (was sub_1402EE0A4). Whole function read. The callers loop over errands 0..95 (the world map town info, the arrival notices).

## Open questions

None recorded.
