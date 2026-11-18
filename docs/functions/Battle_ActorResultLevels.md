# Battle_ActorResultLevels

- **Address:** `0x14030C704`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 Battle_ActorResultLevels(_BYTE *unit, _BYTE *out)`
- **Callers:** sub_14020435C
- **Callees:** Battle_ApplyActionResult, Job_IdToIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the acting unit's action result and returns, in four bytes, what the level-up banners need: two result bytes, the new unit level and the new job level.

## Behavior

- V: returns -1 for an empty slot (unit +1 = 0xFF).
- V: clears the two top bytes of qword_1407B07B0, stores the unit index (+444) in dword_14186AFF4 and calls Battle_ApplyActionResult with g_BattleStateGate set to 1 around it.
- V: out[0] = unit +488, out[1] = unit +489; out[2] = the unit level (+41) when byte 6 of qword_1407B07B0 is set, else 0.
- V: out[3] = the level nibble of the unit's job (Job_IdToIndex of the job byte +3; +228 + index / 2, low nibble for an odd index) when byte 7 of qword_1407B07B0 (set by Battle_AwardActorJp when the job level changed) is set, else 0.
- V: the caller passes the unit's label task +462 as `out`, so out[2] is task +464 (read by Battle_ShowUnitLevelUp) and out[3] task +465 (read by Battle_ShowJobLevelUp).

## State touched

- Calls: [Battle_ApplyActionResult](Battle_ApplyActionResult.md), [Job_IdToIndex](Job_IdToIndex.md)

## Referenced by

- Called by: [sub_14020435C](sub_14020435C.md)

## Notes

Name is ours.

## Open questions

? the meaning of unit +488 / +489 (an earlier read took them for the two halves of a name id: I).
