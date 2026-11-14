# TavernErrandsOpenAtSituationCounter450

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Errands](../areas/errands.md)
- **Affects:** [BarTop_Setup](../functions/BarTop_Setup.md), [UserSituation_IsMet](../functions/UserSituation_IsMet.md), [UserSituation_TestCheck](../functions/UserSituation_TestCheck.md), [UserSituation_SetValue](../functions/UserSituation_SetValue.md), [Errand_IsAvailable](../functions/Errand_IsAvailable.md), [g_UserSituation](../globals/g_UserSituation.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The tavern's errand row is open only when UserSituation 3220 holds: situation counter 0 (the dword at g_UserSituation +24, or +104 with the bank bit) is at least 450, which event opcode 0xE9 raises with the story. Each errand then has its own test (town, story variable 111, prerequisite, delay, state).

## Behavior

- V: nxd UserSituation row 3220 has one entry: check type 6 (counter >= value) on id 0 with value 450, IsTrueForSuccess 0; an entry whose checks all equal that byte makes the answer false.
- I: 450 is the start of Chapter 2 (rows 1010 / 1020 / 1030 band the counter at 445 / 450..1320 / 1330).
- V (owner, live): on a Chapter 1 save the row reads '???'.

## Open questions

? the bank bit (+16 bit 0) of the situation store.
