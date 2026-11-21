# Ai_UnitTurnStep

- **Address:** `0x14031F130`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 Ai_UnitTurnStep(int slot, AiDecision *out)`
- **Callers:** sub_14020AD64
- **Callees:** Battle_AITurnPrepare, Ai_SurveyTargets, sub_14031F92C, sub_14031F68C, sub_14031F794, sub_140320920, sub_14031F464, Mem_CopyChecked

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one step of an AI-controlled unit's decision (several frames per turn) and, when it is done, writes the chosen move and action.

## Behavior

- V: a resumable state machine (stage byte byte_14187257C): Battle_AITurnPrepare, then Ai_SurveyTargets, then the move pass sub_14031F92C and sub_14031F68C / sub_14031F794, then the planner sub_140320920; a stage that is not finished returns -1 and is resumed on the next call.
- V: before the first stage it sets g_BattleSimulating (0x14186AF80) to 1 and saves the 32-byte state at xmmword_14186AFA0; when the planner is done it clears the flag and puts the state back.
- V: the result: out +0 = 0 with the target tile (x, y, layer) at +4 / +6 / +8, or 1 with a copied action block, or 2 (no action); the chosen tile is also written to the acting unit +79 / +80 / +81 bit 7.

## State touched

- Calls: [Battle_AITurnPrepare](Battle_AITurnPrepare.md), [Ai_SurveyTargets](Ai_SurveyTargets.md), [Mem_CopyChecked](Mem_CopyChecked.md)

## Referenced by

- Observed behaviours: [AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable](../behaviors/AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable.md), [TheAiHandlesSixteenUnitsOnTheField](../behaviors/TheAiHandlesSixteenUnitsOnTheField.md)

## Notes

Name is ours.

## Open questions

? the planner sub_140320920 and its candidate loop (sub_14038BC00, sub_14038C95C) are not read yet.
