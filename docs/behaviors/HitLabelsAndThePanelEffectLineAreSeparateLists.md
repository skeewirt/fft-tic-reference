# HitLabelsAndThePanelEffectLineAreSeparateLists

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ResultLabel_QueueFromUnit](../functions/ResultLabel_QueueFromUnit.md), [ResultLabel_ShowNext](../functions/ResultLabel_ShowNext.md), [BattleLabel_ShowStatusSignal](../functions/BattleLabel_ShowStatusSignal.md), [UnitPanel_FillEffectLine](../functions/UnitPanel_FillEffectLine.md), [UnitPanel_SetSignalList](../functions/UnitPanel_SetSignalList.md), [StatusList_BuildFromResultBlock](../functions/StatusList_BuildFromResultBlock.md), [tbl_StatusBattleSignal](../globals/tbl_StatusBattleSignal.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The status label over a unit hit by an action and the effect line of the unit status panel are two different lists. The hit label maps a status to its BattleSignal row through the fixed 40-byte tbl_StatusBattleSignal; the panel maps it through UIStatusEffect (field +20 non-zero, field +24 the BattleSignal row). Both start from the result block's 40-bit added and removed sets.

## Behavior

- V (traced live 2026-11-17): StatusList_BuildFromResultBlock and UnitPanel_SetSignalList ran while the action preview was up and on enemy turns, and not when the action's result showed over the hit unit.
- V (code read): the hit labels never read UIStatusEffect to choose the row; only the icon is looked up there, by the BattleSignal key.
- V (seen live 2026-11-17): a status outside the 40-bit sets showed no label over the hit unit; with its BattleSignal id appended to the task queue after the game's walk, it showed its title and its own icon.
- V (seen live 2026-11-17): the action preview resolves the action with the forecast mode 2 (the dword at 0x14186AF80); the result shown over the hit unit comes from the action's real pass (mode 0).
- I (traced live 2026-11-17): after the pass on the target, Battle_ResolveAction ran again with the acting unit as its target; the target then countered (Counter shown), so the second pass is taken to be the reaction check.

## Open questions

None recorded.
