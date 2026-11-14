# g_ErrandFinishDay

- **Kind:** global
- **Address:** `0x1411A70D0`
- **Type:** `errands`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint8[108]: the finish date of each errand as 9 bits (day 5 bits, month 4 bits) at bit 9 * errand: 96 x 9 bits = 108 bytes (DateBits_Store9), saved with the game (world save field mouke_finishday). Written by Errand_ApplyResult on success, copied by the save pack / unpack / copy functions

## Referenced by

- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)
- Written by: [DateBits_Store9](../functions/DateBits_Store9.md)

## Open questions

None recorded.
