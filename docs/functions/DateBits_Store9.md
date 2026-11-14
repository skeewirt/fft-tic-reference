# DateBits_Store9

- **Address:** `0x1402CD274`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void DateBits_Store9(uint8_t *bits, int index, const uint8_t date[2])`
- **Callers:** Errand_ApplyResult
- **Callees:** sub_14036D1E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores a date (month, day) as 9 bits at position 9 * index of a bit array: the errand finish dates and the treasure find dates.

## Behavior

- V: writes the five low bits of date[1] (the day) to bits 9 * index .. 9 * index + 4 and the four low bits of date[0] (the month) to the next four, one bit per call of sub_14036D1E4(bits, bit, value).
- V (arguments of the caller, not this body): Errand_ApplyResult passes g_ErrandFinishDay with the errand, and the two treasure date arrays (the 9-bit arrays after the active slots) with the treasure index.

## State touched

- Writes: [g_ErrandFinishDay](../globals/g_ErrandFinishDay.md)

## Referenced by

- Called by: [Errand_ApplyResult](Errand_ApplyResult.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Notes

Name is ours (was sub_1402CD274). So g_ErrandFinishDay is 96 x 9 bits = 108 bytes.

## Open questions

None recorded.
