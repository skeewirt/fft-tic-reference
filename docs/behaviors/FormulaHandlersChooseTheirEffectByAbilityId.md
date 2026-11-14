# FormulaHandlersChooseTheirEffectByAbilityId

- **Kind:** observed behaviour
- **Scope:** engine (battle formulas)
- **Area:** [Battle formulas](../areas/formulas.md)
- **Affects:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [BattlePreview_BuildAction](../functions/BattlePreview_BuildAction.md), [sub_1403064D8](../functions/sub_1403064D8.md), [Action_PickTargetEquipment](../functions/Action_PickTargetEquipment.md), [Formula_28_BardSongs](../functions/Formula_28_BardSongs.md), [Formula_29_DancerDances](../functions/Formula_29_DancerDances.md), [Formula_42_Speechcraft](../functions/Formula_42_Speechcraft.md), [g_FormulaBlock](../globals/g_FormulaBlock.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Several shared formula handlers choose their effect by the ability id in the formula block's word +8, and the resolver tests a few single ids, so an ability id none of them lists takes the default branch (usually: no effect).

## Behavior

- V: the sap effect (sub_1403064D8, called by Formula_26_StatSap and Formula_43_RendStats): ids 143, 144, 145 and 197, 198, 199; any other id does nothing.
- V: the equipment steal chain (Action_PickTargetEquipment): ids 110..114, 138..141, 160..163 and 361..365 pick which equipped item is taken; any other id returns -1 with no item.
- V: songs (Formula_28_BardSongs): 86..92; dances (Formula_29_DancerDances): 93..99; Speechcraft (Formula_42_Speechcraft): 117..121 and 123; any other id gets the default branch, which only sets the result flag in the songs and dances.
- V: single-id tests the resolver and others make: 65 (Golem) at 0x140305F52 in sub_140305F4C; 219 at 0x140306C30 in sub_140306C10; in Battle_ResolveAction id 358 keeps the inflict index already in the block instead of the action row's byte +11 (0x140309D67) and id 357 skips the clear of the weapon or item word (0x140309D8B); BattlePreview_BuildAction tests 357 at 0x140282306 on the unit's ability word (+0x1A2).
- V: Battle_ResolveAction copies the 20-byte action row (the row of the id, or row 0 for an id above 0x16F) to 0x1407B0794 before it dispatches the formula; the formula id is row byte +8, clamped to 1 when it is above 0x6A, and the handler is g_FormulaHandlers[formula].
- V: the sap function has the cases 143..145 and 197..199; Speechcraft has no case for 122.

## Notes

The word is the one at 0x1407B0778 = block + 8.

## Open questions

? every other handler that tests the word (the 14 readers are listed on g_FormulaBlock; only the five above were read in full).
