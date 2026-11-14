# UserSituation_TestCheck

- **Address:** `0x1400FFAF0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool UserSituation_TestCheck(void *unused, unsigned int type, unsigned int id, unsigned int id2, unsigned int value, unsigned int value2)`
- **Callers:** UserSituation_IsMet
- **Callees:** SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One check of a UserSituation row against the situation store (qword_143CD9DE0): a flag byte, a counter compare or a scene variable.

## Behavior

- V: the store has two banks chosen by bit 0 of its byte +16: flags at +72 / +152 (one byte per id), counters at +24 / +104 (one dword per id).
- V: type 1 / 2 = flag set / clear; 3 = counter == value; 4 <=; 5 <; 6 >=; 7 >; 8..11 = a range of counter id (8: >= value, 10: > value) together with counter id2 (8, 10: <= value2; 9, 11: < value2); 12..15 = SceneVar_Read(id) equals the type; 16 = SceneVar_Read(id) - 12 <= 3.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)
- Reads: [g_UserSituation](../globals/g_UserSituation.md)

## Referenced by

- Called by: [UserSituation_IsMet](UserSituation_IsMet.md)
- Observed behaviours: [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md)

## Notes

Name is ours (was sub_1400FFAF0). Whole function read.

## Open questions

? what selects the second bank (byte +16 bit 0).
