# Battle_ResolveAction

- **Address:** `0x1403099B0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t Battle_ResolveAction(const void *request, uint8_t targetSlot)`
- **Callers:** `Battle_ResolveTargets` (`0x140281F0D`), `sub_140283C00` (`0x140283CF2`, reaction path), `Formula_37_RendEquipment` (`0x140307ED4`, second hit)
- **Callees:** memcpy (`sub_14002630C`), `sub_1403095E4`, `Action_SetWeaponItem`, `sub_140309540`, `Item_FindCategoryIndex`, `Item_GetWeaponRecord`, `AbilityAction_GetRecord`, `sub_14030A410`, `sub_14030AFEC`, `Item_IsInCategory`, `Item_GetChemistRecord`, the formula handler table, `sub_1403067D0`, `sub_14030A11C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves one action request against one target: selects the formula from the action type / ability, runs
the formula handler and leaves a 40-byte result record for the apply step. This is the only caller of the
`g_FormulaHandlers` table (`0x140682BC8`) besides the F106 re-dispatch.

## Behavior

- V: copies the 20-byte request from `a1` to the stack (`0x1403099E8`); byte 0 is the actor slot,
  byte 1 the action type, word +2 the ability id.
- V: sets the working pointers: `qword_14186AF78` = live record[actor], `qword_14186AF68` = live
  record[target], `qword_14186AF70` = live record[target] + `0x1BE` (result).
- V: picks the formula by action type `byte_14067E010[type]`:
  - 0/3/6: weapon formula from the weapon record (`WeaponRecord[2]`, `0x140309B7C`);
  - 1: item/chemist record (`Item_GetChemistRecord`, `0x140309E63`);
  - 2: formula 99; 4: terrain formula (`byte_14067F750[...]`); 7/8/9/10: ability table / specials.
- V: ability id -> `AbilityAction_GetRecord` (`0x140309B95`, `0x140309D41`), copies the 20-byte ability
  action record to `xmmword_1407B0790+4`; formula = record `+8`, element `+7`, inflict `+11`,
  CT `+12`, MP `+13`.
- V: `sub_14030AFEC` (`0x140309E19`) runs the pre-formula reaction/status guards.
- V: calls the handler as `g_FormulaHandlers[formulaId]` at `0x140309F53`; formula 106 is the
  re-dispatch entry.
- V: afterwards `sub_14030A11C` (`0x140309F78`) clamps damage/heal to 999 and clears result flags.
- V: the result record is not applied here; `Battle_ApplyActionResults` reads it later.
- V (2026-11-10): the working pointers are set from the arguments: 0x14186AF78 = the record of the request's actor slot (request byte 0), g_BattleActingUnit (0x14186AF68) = the record of the target slot (the second argument); when the battle-state gate 0x14186AF9C is non-zero, sub_1403095E4 (the reaction executor) runs first and a non-zero answer ends the resolve through Action_SetWeaponItem.
- V: the ability id is the request's word +2 (stored in the formula block's word +8 at 0x1407B0778; the two writes are at 0x140309B6A and 0x140309C42); the 20-byte action row is copied to 0x1407B0794 (the row of the id, or row 0 for an id above 0x16F, a compare with 0x170; the second copy for kinds 0, 3, 6 and 7 happens only for an id below 368, else the default formula 1 is used).
- V: id 358 keeps the inflict index already in the block instead of the action row's byte +11 (test at 0x140309D67), and id 357 skips the clear of the weapon or item word (test at 0x140309D8B); the formula id is action-row byte +8, clamped to 1 when above 0x6A (a compare of formula - 1 with 0x69), and the handler is g_FormulaHandlers[formula]. See FormulaHandlersChooseTheirEffectByAbilityId.
- V: a Charge clamp for command type 10 sits at 0x140309EB8.

## State touched

- Calls: [sub_1403095E4](sub_1403095E4.md), [Action_SetWeaponItem](Action_SetWeaponItem.md), [Item_FindCategoryIndex](Item_FindCategoryIndex.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [sub_14030AFEC](sub_14030AFEC.md), [Item_IsInCategory](Item_IsInCategory.md), [sub_1403067D0](sub_1403067D0.md), [sub_14030A11C](sub_14030A11C.md), [Mem_CopyChecked](Mem_CopyChecked.md)
- Writes: [FormulaBlock](../structs/FormulaBlock.md), [g_BattleCasterUnit](../globals/g_BattleCasterUnit.md), [g_BattleCasterResult](../globals/g_BattleCasterResult.md), [ActionResult](../structs/ActionResult.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Battle_ResolveReaction](Battle_ResolveReaction.md), [Battle_ResolveTargets](Battle_ResolveTargets.md)
- Observed behaviours: [BattleItemsAreUsedThroughItemAbilities](../behaviors/BattleItemsAreUsedThroughItemAbilities.md), [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md), [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md), [FormulaIdsPastTheByte](../behaviors/FormulaIdsPastTheByte.md), [ItemCommandRelation](../behaviors/ItemCommandRelation.md), [SkillsetIdsPastTheByte](../behaviors/SkillsetIdsPastTheByte.md), [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md), [StockFormulaHandlersAreBlockSequences](../behaviors/StockFormulaHandlersAreBlockSequences.md)

## Notes

The request at unit `+0x1A0` is built by `sub_140282E38` for queued/charged abilities and by the battle
menu for immediate commands (menu path not traced; C3).

## Open questions

- The exact menu site that writes the request.
- What each action type 7/8/9/10 means (only the formula selection is read).
