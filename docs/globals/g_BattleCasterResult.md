# g_BattleCasterResult

- **Kind:** global
- **Address:** `0x14186AF60`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `ActionResult *`
- **Points to / is a:** [ActionResult](../structs/ActionResult.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer to the caster's own result block of the action being resolved: a static ActionResult at 0x14186AFC0, apart from the unit records. A handler writes here an effect on the caster (a drain's heal, a stolen gil, a recoil). IDA names it qword_14186AF60.

## Behavior

- V: Battle_ResolveAction stores the address of the static block (0x14186AFC0) here (0x140309A46) and resets it with Battle_ResultReset after the target's block.
- V: written through this pointer by Formula_DrainHP, Formula_DrainMP, Formula_DrawOutGate, Formula_StealGilApply and formulas 40, 60, 66, 87 and 91 (hit flag 1, amount, kind bit); read by sub_14030A11C, Battle_ExecuteSecondaryAction and the reaction code.

## Referenced by

- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)
- Read by: [BattleTask_ActorForecastPanel](../functions/BattleTask_ActorForecastPanel.md)
- Written by: [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Formula_DrainHP](../functions/Formula_DrainHP.md), [Formula_DrainMP](../functions/Formula_DrainMP.md)

## Notes

Checked 2026-11-12. The name is proposed.

## Open questions

? how the result applier orders the caster's block against the target's.
