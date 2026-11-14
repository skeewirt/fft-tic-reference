# FormulaHandlerContract

- **Kind:** observed behaviour
- **Scope:** The 106 ability formula handlers and the blocks they call
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [sub_14030A11C](../functions/sub_14030A11C.md), [Formula_ZeroResult](../functions/Formula_ZeroResult.md), [Formula_ChanceRoll](../functions/Formula_ChanceRoll.md), [Formula_DamageAB](../functions/Formula_DamageAB.md), [Formula_DrainHP](../functions/Formula_DrainHP.md), [Formula_DrainMP](../functions/Formula_DrainMP.md), [Formula_StatusChance19](../functions/Formula_StatusChance19.md), [ActionResult](../structs/ActionResult.md), [FormulaBlock](../structs/FormulaBlock.md), [g_BattleActionBlock](../globals/g_BattleActionBlock.md), [g_BattleCasterResult](../globals/g_BattleCasterResult.md), [g_BattleCasterUnit](../globals/g_BattleCasterUnit.md), [g_BattleActingUnit](../globals/g_BattleActingUnit.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What a formula handler may assume and has to leave behind, read from the stock handlers and from Battle_ResolveAction: the frame it is called in, how it says 'no effect', which result fields go together, why it must not roll during a preview, the two-sided result, the post-processing it does not control, and the ability ids the shared blocks compare.

## Behavior

- V: frame: a handler is entered through call [r12 + rax * 8] with no argument and its return value ignored (0x140309F53); everything it needs is in globals: the caster unit (g_BattleCasterUnit), the target unit (g_BattleActingUnit), the target's result block (g_BattleActionBlock), the caster's result block (g_BattleCasterResult) and g_FormulaBlock (record copies at 0x1407B0794, the weapon at 0x1407B07A8, the inflict row at 0x1407B07B0, the item id at +0x0A, the inflict row index at +0x0D, the faith bytes at +4 / +5, the weapon bonus at +0x17).
- V: both result blocks were reset by Battle_ResultReset just before (hit flag 1, hit percent 100, the rest 0), so a handler only has to lower the hit flag or fill amounts.
- V: no effect: the stock idiom is hit = 0, reason (5 nullified, 6 failed chance, 7 no effect) and hit percent 0, with the amounts left 0; Formula_ChanceRoll also zeroes the amount.
- V: amounts and kind bits go together: the four amount words are signed; every routing block sets the matching kind bit (0x80, 0x40, 0x20, 0x10; 0x08 for a pending status; 0x01 for a stat, gil or EXP change). sub_14030A11C's caller sets kind bit 0x01 afterwards when the flag word is non-zero.
- V: preview and the AI share the handler: g_BattleSimulating is non-zero during a forecast; Battle_Rand15 then returns 0x4000, Formula_ChanceRoll skips its roll unless the chance is 0, Formula_EvadeByteRoll and Formula_BardDancerGate skip their rolls, and the value 2 is tested by Formula_56_StatusOnlyApplication (every listed status dropped on the 24 percent roll) and Formula_StatusChance19 (returns false).
- V: two-sided results: an effect on the caster is written to the caster's block with its hit flag 1, the amount word and the kind bit (Formula_DrainHP, Formula_DrainMP, formulas 39, 40, 60, 66, 91); Formula_87 swaps the unit pointers instead. The resolver applies both blocks (I).
- V: post-processing the handler does not control: sub_14030A11C(1) clamps the four amounts to 999, scales HP and MP damage by the difficulty row (only when g_ShopModeGate is non-zero and the unit flag bits at +0x1EE say so), runs the hook row of formulas 6, 14, 15, 16, 23, 47, 48, 71, 72, 74, 75 and 77 only, and clears the hit flag when the hit percent is 0. A formula id with no hook row gets no Undead rule from it; Formula_DrainHP and Formula_DrainMP call the function with 0 themselves.
- V: ids the shared blocks compare: the stored formula id (g_FormulaBlock +0x18) is tested by ten sites (7, 106, 37, 38, 39, 40, 46, 42, 99 and two membership sets); the post step sub_1403067D0 runs only for stored ids below 7; id 100 clears the item word; id 3 uses inflict row 0.
- V: ability-id keyed blocks: Formula_StatusChance19 (219), Formula_ChanceSum (65), Formula_SapStatPick (143 to 145 and 197 to 199), Action_PickTargetEquipment (18 ids), and formulas 28, 29 and 42 read the ability word at g_FormulaBlock +8.
- V: inflict: the statuses a handler adds come from the six-byte inflict record copy chosen by g_FormulaBlock +0x0D (the weapon record's byte +7, the chemist record's byte +2 or the ability record's byte +0x0B; formula 3 forces row 0); Formula_56_StatusOnlyApplication applies it, or the handler writes ActionResult +0x1D..+0x26 itself.

## Notes

Checked 2026-11-12.

## Open questions

? how the result applier consumes the caster's block in every case (I: it applies both); whether a handler may leave the flag word unset when it writes kind bit 0x01 itself.
