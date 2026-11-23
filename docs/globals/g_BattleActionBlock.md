# g_BattleActionBlock

- **Kind:** global
- **Address:** `0x14186AF70`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `ActionResult *`
- **Points to / is a:** [ActionResult](../structs/ActionResult.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer to the result block of the current action on its target: unit +0x1BE of the target's slot (the formula handlers' R). The reaction helpers read the reaction id at +0x10 and the miss reason at +2; +0x2C is the hit percent.

## Behavior

- V: sub_14030AFEC loads it and writes the ability, the CT spend and the kind.
- V: Battle_ResolveAction stores it (0x140309A2D) as g_PreviewUnitTable + 0x1BE + 512 * (request byte 1) and resets it with Battle_ResultReset; every formula handler and block writes its result through it (struct ActionResult). The caster's own result block is g_BattleCasterResult.

## Referenced by

- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)
- Read by: [BattleTask_ActorForecastPanel](../functions/BattleTask_ActorForecastPanel.md), [BattleTask_TargetForecastPanel](../functions/BattleTask_TargetForecastPanel.md), [sub_14030AFEC](../functions/sub_14030AFEC.md)
- Written by: [sub_14030AFEC](../functions/sub_14030AFEC.md)

## Open questions

None recorded.
