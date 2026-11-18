# Ai_SurveyTargets

- **Address:** `0x14031FD40`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Ai_SurveyTargets(int flag)`
- **Callers:** Ai_UnitTurnStep
- **Callees:** Action_BuildCurrentAction, Ai_ActionWorthOnUnit, Ai_StatusLastsTurns, Item_GetRecord, sub_140321704, sub_14038E2AC, sub_1403170CC, sub_140320490

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Before planning, goes over every unit and every action in the acting unit's action list and notes what those actions could do to each unit (hurt it, help it), then marks which of its own actions are worth planning with.

## Behavior

- V: for each of the 21 units and each of the 34 entries of its row in g_AiCommandTable (ended by 0xFF) it fills g_AiCurrentAction with Action_BuildCurrentAction and skips actions the unit cannot use (statuses 37 Disable, 33 Atheist, the ability gates, items not held: g_InventoryCounts).
- V: it counts the actions whose flag byte (g_AiCurrentAction +13) has bit 0x02 (they hurt) and bit 0x01 (they help), and from them sets bits 0x01 / 0x02 / 0x04 of the unit's AI byte (byte_141872EDE + 16 x slot).
- V: then for the acting unit's own list it drops some entries when nothing needs them (sub_140320490 with 27, 26, 38, 17) and, for each remaining one, asks Ai_ActionWorthOnUnit whether it is worth trying on the acting unit itself (entry flag bit 0x01).
- V: it keeps the shortest reach of a hurting action and of a helping one (+14 / +15 of the record at qword_1418724D8).
- V: for a command of kind 2 (Throw) it walks ability ids 383..392 (sub_1403170CC for availability), then item ids 0..255 (Item_GetRecord), keeping the item whose record byte +5 matches the throw category; the pick goes to word_1418724B4 / byte_1418724B6.
- V: the slot test at 0x14032003F (v5 != 255) is a battle-unit sentinel, not an item id.

## State touched

- Calls: [Action_BuildCurrentAction](Action_BuildCurrentAction.md), [Ai_ActionWorthOnUnit](Ai_ActionWorthOnUnit.md), [Ai_StatusLastsTurns](Ai_StatusLastsTurns.md), [Item_GetRecord](Item_GetRecord.md), [sub_1403170CC](sub_1403170CC.md)

## Referenced by

- Called by: [Ai_UnitTurnStep](Ai_UnitTurnStep.md)
- Observed behaviours: [AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable](../behaviors/AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable.md)
- Reads tables: [AbilityKind2_ThrowCategory](../tables/AbilityKind2_ThrowCategory.md)

## Notes

Name is ours.

## Open questions

? the exact meaning of each AI byte bit and of the ratio test (count x 128 / total, threshold 76).
