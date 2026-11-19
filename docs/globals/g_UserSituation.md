# g_UserSituation

- **Kind:** global
- **Address:** `0x143CD9DE0`
- **Type:** `event system`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

pointer to the situation store UserSituation_TestCheck reads: a bank flag byte at +16 (bit 0), flag bytes at +72 / +152, dword counters at +24 / +104. Counter 0 >= 450 opens the tavern errands (situation 3220). Written by UserSituation_SetValue (event opcode 0xE9) and its flag twin (0xEA), saved with the game (SaveWork_PackFromLive)

## Referenced by

- Observed behaviours: [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md)
- Read by: [UserSituation_TestCheck](../functions/UserSituation_TestCheck.md)
- Written by: [EventViewer_StartReplay](../functions/EventViewer_StartReplay.md), [UserSituation_SetValue](../functions/UserSituation_SetValue.md)

## Open questions

None recorded.
