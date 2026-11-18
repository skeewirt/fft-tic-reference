# Ai_ActionWorthOnUnit

- **Address:** `0x14038B34C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Ai_ActionWorthOnUnit(int slot, int self)`
- **Callers:** Ai_SurveyTargets, sub_1403883C0, sub_140388ABC, sub_14038B2F8
- **Callees:** Ai_StatusLastsTurns, AbilityAction_GetRecord, sub_14038E2AC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells the AI whether the action in g_AiCurrentAction is worth trying on unit `slot`: 0 no, 1 yes, 2 yes (a stronger case).

## Behavior

- V: 0 when the unit will still be Jumping (5) when the action resolves; when it will still have Reflect (38) and the action has hint bit +14 0x40 (the self test only), or Atheist (33) and hint bit +14 0x04 (I: reflectable and faith-based actions); when status 31 will last and the action lacks hint bit +11 0x01.
- V: an action that adds statuses (g_AiCurrentAction +13 bit 0x10): for each of the five status bytes, the action's bits (+8..+12) that the unit does not have (+0x61..+0x65) and is not immune to (the 5 bytes at +0x5C) make it worth it (with exceptions per byte: some statuses only when other conditions hold).
- V: an action that removes statuses (cancel mode): the bits the unit has (+0x61..) and that are not innate (the 5 bytes at +0x57) make it worth it; for statuses 24 and up only when Ai_StatusLastsTurns says they will not wear off before the action resolves.
- V: so only the 40 statuses of the five status bytes enter this test.
- V: when the unit is the acting unit and the action id is below 368, an action whose AbilityAction record +4 has bit 0x01 is not worth it (the id gate at 0x14038B3DD).
- V: the random pass of hint bit +13 0x08 steps the game xorshift state (xmmword_1408E5FC8).

## State touched

- Calls: [Ai_StatusLastsTurns](Ai_StatusLastsTurns.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Referenced by

- Called by: [Ai_SurveyTargets](Ai_SurveyTargets.md)
- Observed behaviours: [AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable](../behaviors/AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable.md)

## Notes

Name is ours.

## Open questions

? the case of the action flag bit 0x08 (abilities 118..150 with a random pass).
