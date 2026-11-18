# AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Ai_UnitTurnStep](../functions/Ai_UnitTurnStep.md), [Ai_SurveyTargets](../functions/Ai_SurveyTargets.md), [Ai_ActionWorthOnUnit](../functions/Ai_ActionWorthOnUnit.md), [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md), [Battle_AITurnRun](../functions/Battle_AITurnRun.md), [tbl_AiStatusValue](../globals/tbl_AiStatusValue.md), [g_AiCurrentAction](../globals/g_AiCurrentAction.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An AI-controlled unit weighs statuses in two places, both limited to the 40 statuses of the five status bytes: the test of whether an action is worth trying on a unit compares the action's status bytes (from its inflict row) with the unit's, and the score of a simulated outcome adds one fixed value per status the unit has (tbl_AiStatusValue).

## Behavior

- V (code read): Action_BuildCurrentAction copies the 5 status bytes of the action's inflict row into g_AiCurrentAction +8..+12 and the ability's AI hint bytes (aux row +4..+7) into +13..+16.
- V (code read): Ai_ActionWorthOnUnit finds an action worth trying when it would add a status the unit lacks and is not immune to, or remove one the unit has, is not innate and will not wear off before the action resolves.
- V (code read): Battle_AITurnRun scores the simulated outcome per unit as HP x 128 / max HP, plus tbl_AiStatusValue[s] for each status s (0..39) the unit has (Blindness and Silence scaled by a unit value / 4; Charmed, Vampire, Confusion halved under some conditions), plus an MP term; units of the acting side count positive, the others negative.
- V (code read): the scale: full HP is worth 128, KO -192, Poison -26, Haste +19.
- V (code read): the AI's trials run with g_BattleSimulating (0x14186AF80) set; Ai_UnitTurnStep sets it before the first stage and clears it when the planner is done.
- ?: whether the simulation runs later turns (turn-end damage, status countdowns) before the score is taken.

## Open questions

None recorded.
