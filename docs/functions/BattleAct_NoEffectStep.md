# BattleAct_NoEffectStep

- **Address:** `0x140206758`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleAct_NoEffectStep(void)`
- **Callers:** BattleAct_Step, sub_140210AF0
- **Callees:** sub_140204CDC, sub_14030A488, sub_140260ABC, Battle_ApplyActionResult, sub_140283784, sub_140269790, BattleAnim_SelectMotion, sub_14027192C, sub_140268EE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the resolved action to every target and starts each target's hit motion: the step that turns the formula results into HP, MP and status changes and visible hits. Runs at once for an action without an effect file, and as battle state 43 after an effect has played.

## Behavior

- V: sets dword_140C6B1CC = 44 (0x140206770), gets the acting scene object (sub_14026079C) and clears its animation word +0x0C.
- V: loops over the target list of the acting object (count +0x1A9, slots +0x1AA): for each slot gets its scene object (sub_140260ABC), calls Battle_ApplyActionResult(slot) at 0x1402067DF and stores the return value on the target object.
- V: on a return of -1 it calls sub_140283784(slot, unit record +0x1A0) (the action request clean-up) and sub_140268F68 (KO and crystal handling).
- V: on the first successful hit it sets the target's +0x1F5 = the actor's slot and adds one to the actor's hit counter at BattleControl + 4 * slot + 0xA94D4 (capped at 9999).
- V: effect word 512: copies the object's bytes +0x1C4..+0x1C6 to each target and calls sub_14027192C (the sentinel case).
- V: word 0 (or a weapon flag case): sub_140269790 (the weapon attack motion); otherwise, when +0x1BF is 0, BattleAnim_SelectMotion.
- V: for each target its action leaves at 0 HP (+0x30) it writes the acting unit's record index (+0x1BC) to the target's +0x1F5 and adds 1 to that record's KO count at g_BattleControl +0xA9494 + 4 x record, capped at 9999 (record BattleKoCountsAndGreatestContribution).

## State touched

- Calls: [Battle_ApplyActionResult](Battle_ApplyActionResult.md), [BattleAnim_SelectMotion](BattleAnim_SelectMotion.md)

## Referenced by

- Called by: [BattleAct_Step](BattleAct_Step.md)
- Observed behaviours: [BattleKoCountsAndGreatestContribution](../behaviors/BattleKoCountsAndGreatestContribution.md)

## Notes

BattleControl is the singleton at 0x143CD9EF0; the hit counter table starts at +0xA94D4. A delayed copy of the apply loop exists in sub_1402029DC. Earlier sheet name: Battle_ApplyActionResults.

## Open questions

Whether the loop applies every target in one pass or one per frame (the call from sub_140210AF0 is a state, so likely one pass).
