# Battle_AwardActorJp

- **Address:** `0x14030C7C4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_AwardActorJp(void)`
- **Callers:** the battle action result code
- **Callees:** Job_IdToIndex, Unit_AwardJobJp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives the acting battle unit its JP for the current job and reports whether its job level changed (for the level-up message).

## Behavior

- V: the unit is the battle record in `qword_14186AF68`; its job index comes from Job_IdToIndex(unit +3).
- V: reads the level byte before, calls Unit_AwardJobJp(unit +444, JP from +489, team bits of +494, index), reads the level byte after.
- V: when the nibble of the job differs, sets the top byte of `qword_1407B07B0` to 1 (the 'job level up' flag of the result).

## State touched

- Calls: [Job_IdToIndex](Job_IdToIndex.md), [Unit_AwardJobJp](Unit_AwardJobJp.md)

## Referenced by

- Called by: [Battle_ApplyActionResult](Battle_ApplyActionResult.md)
- Observed behaviours: [BattleJpGoesToTheJobOfTheUnitsByteNotItsClass](../behaviors/BattleJpGoesToTheJobOfTheUnitsByteNotItsClass.md)

## Open questions

I: the JP amount at +489 is computed by the action code before this call (not traced).
