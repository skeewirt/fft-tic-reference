# Job_IdToIndex

- **Address:** `0x1402B8F18`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `int Job_IdToIndex(int16_t jobId)`
- **Callers:** Job_IsLockedForParty, sub_1402867BC, Unit_BuildJobUnlockMask
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a job key to its tree/unlock index.

## Behavior

- V: 74..93 -> 0..19.
- V: 160, 161 -> 20, 21 (id - 140).
- V: anything else -> 0.
- V: the index, not the job id, selects the per-job arrays: unlock rows, job-level nibbles, JP arrays, learned-bit groups and GeneralJob rows. JobTable and the unit's job byte use the id.
- V: also called by Job_LearnAbilityByMenu and the job-list helper sub_1402867BC.

## Referenced by

- Called by: [Battle_AwardActorJp](Battle_AwardActorJp.md), [Battle_AwardUnitJp](Battle_AwardUnitJp.md), [Errand_ApplyResult](Errand_ApplyResult.md), [JobAbilityList_Build](JobAbilityList_Build.md), [JobRecord_FromJobId](JobRecord_FromJobId.md), [JobScreen_BuildLearnableList](JobScreen_BuildLearnableList.md), [JobScreen_FillUnitRows](JobScreen_FillUnitRows.md), [Job_IsLockedForParty](Job_IsLockedForParty.md), [Job_LearnAbilityByMenu](Job_LearnAbilityByMenu.md), [Job_ReadLearnedBitsForBattle](Job_ReadLearnedBitsForBattle.md), [Party_CountMasteredJobs](Party_CountMasteredJobs.md), [UnitWork_StoreToSaveSlot](UnitWork_StoreToSaveSlot.md), [Unit_BuildJobUnlockMask](Unit_BuildJobUnlockMask.md), [Unit_QueueJobAbilitiesToLearn](Unit_QueueJobAbilitiesToLearn.md), [Unit_SpendJp](Unit_SpendJp.md), [sub_1401321FC](sub_1401321FC.md), [sub_14028A474](sub_14028A474.md), [sub_14030C704](sub_14030C704.md), [sub_14030CD08](sub_14030CD08.md), [sub_14030E368](sub_14030E368.md), [sub_1403170CC](sub_1403170CC.md), [sub_140367AA0](sub_140367AA0.md), [sub_140392620](sub_140392620.md), [sub_140392800](sub_140392800.md), [sub_14039284C](sub_14039284C.md), [sub_140392884](sub_140392884.md), [sub_1403928D4](sub_1403928D4.md), [sub_14039297C](sub_14039297C.md)
- Observed behaviours: [BattleActionJpFormulaAndSpillover](../behaviors/BattleActionJpFormulaAndSpillover.md), [BattleJpGoesToTheJobOfTheUnitsByteNotItsClass](../behaviors/BattleJpGoesToTheJobOfTheUnitsByteNotItsClass.md), [GenericUnitSpriteNumberFromJob](../behaviors/GenericUnitSpriteNumberFromJob.md), [PerJobSlotStateLayouts](../behaviors/PerJobSlotStateLayouts.md)
- Resolves registries: [JobIdSpace](../registries/JobIdSpace.md)

## Notes

The ids 160 and 161 are hard-coded here, as are the 0xA0 base-constant sites elsewhere.

Ids 94 and above (monsters) and ids below 74 (special characters) all return index 0, so they collide with Squire in any per-index array.

- Correction (J7 report): 34 callers in the J7 census (J9 counted 37 sites in 33 functions with its own method).

## Open questions

None recorded.
