# BattlePanelJobLineShowsDashesAtLevelZero

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [UnitPanel_FillJobLine](../functions/UnitPanel_FillJobLine.md), [BattleMain_SetPanelJobRecord](../functions/BattleMain_SetPanelJobRecord.md), [BattleUnit_BuildJobRecord](../functions/BattleUnit_BuildJobRecord.md), [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The job line of a battle unit panel shows 'Lv. --' and '--' for JP and next whenever the job record's level is 0. The record is built from copies of the unit's level and JP arrays: BattleUnit_BuildJobRecord copies them into its own stack frame and JobRecord_FromJobId reads the copies; BattleMain_SetPanelJobRecord stores the result for the panel.

## Behavior

- V (code read): UnitPanel_FillJobLine tests the level (record +68) first; at 0 or less every number of the line is replaced by the dash text.
- V (traced live 2026-11-17): moving the cursor onto a unit called JobRecord_FromJobId from BattleUnit_BuildJobRecord with the frame copies of the arrays, then BattleMain_SetPanelJobRecord from Battle_UnitStatusFillAlt with that record.
- V (seen live 2026-11-17): monsters (all job level nibbles 0) show the dashes.
- V (code read): every generic job of a spawned human unit starts at level 1 or more (UnitWork_InitFromSpawnRecord) with 100..199 JP (Unit_InitJobJp), and level 1 needs 100 JP on the stock curve, so a human unit's own job never shows the dashes.

## Open questions

None recorded.
