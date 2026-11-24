# Unit_AwardJobJp

- **Address:** `0x140283664`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int Unit_AwardJobJp(int battleUnit, int jp, char team, unsigned int jobIndex)`
- **Callers:** sub_14030C7C4 (the acting unit's award, index from Job_IdToIndex)
- **Callees:** sub_140278D5C (level from total JP), Unit_BuildJobUnlockMask

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds JP to one job of a battle unit: current JP and total JP (both capped at 9999), recomputes the job's level from the total and rebuilds the unit's unlock mask. The battle JP award goes through it.

## Behavior

- V: the unit is record `battleUnit` of the 21 battle work records (512 bytes each); returns -1 when the slot is empty (+1 = 0xFF), when flags at +97 (0x60) or +98 (bit 0) or +6 (0x20) are set, or when the team bits at +494 differ from `team`.
- V: job index 17 is refused while flag +6 bit 6 is set, job index 18 while +6 bit 7 is set.
- V: JP at +240 + 2*jobIndex and total JP at +286 + 2*jobIndex get `jp` added, each capped at 9999.
- V: the level nibble at +228 + jobIndex/2 (low nibble for odd indices) becomes the number of levels 1..8 whose job_level_jp (GeneralJob row = jobIndex) the new total reaches (`sub_140278D5C`).
- V: then `Unit_BuildJobUnlockMask(+228, +6, +162, +500)` and the 24-bit result is stored big-endian at +159..161.
- V: returns 0 after an award.

## State touched

- Calls: [Unit_BuildJobUnlockMask](Unit_BuildJobUnlockMask.md)

## Referenced by

- Called by: [Battle_AwardActorJp](Battle_AwardActorJp.md), [Battle_AwardUnitJp](Battle_AwardUnitJp.md)
- Observed behaviours: [AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget](../behaviors/AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget.md), [BattleActionJpFormulaAndSpillover](../behaviors/BattleActionJpFormulaAndSpillover.md), [BattleJpGoesToTheJobOfTheUnitsByteNotItsClass](../behaviors/BattleJpGoesToTheJobOfTheUnitsByteNotItsClass.md)

## Open questions

None recorded.
