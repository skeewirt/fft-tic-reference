# g_AiCurrentAction

- **Kind:** global
- **Address:** `0x1418716A0`
- **Type:** `battle ai`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

16 bytes (+0x10 / +0x20 more): the action the AI is looking at, filled by Action_BuildCurrentAction: +0 command, +1 its charge time (I: AbilityAction +12; added to turn counts), +2 ability id (word), +4 a byte (? range), +6 a word, +8..+12 the statuses it adds or removes (the 5 status bytes of its inflict row, read at dword_14080FBA1 + 6 x row), +13..+16 the ability's AI hint bytes (its aux row +4..+7; +13 bit 0x02 = the action hurts, 0x01 = it helps (counted so by Ai_SurveyTargets), 0x10 = it changes statuses (I))

## Referenced by

- Observed behaviours: [AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable](../behaviors/AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable.md), [TheAiHandlesSixteenUnitsOnTheField](../behaviors/TheAiHandlesSixteenUnitsOnTheField.md)

## Open questions

None recorded.
