# UnitPanel_FillEffectLine

- **Address:** `0x140227CF8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 UnitPanel_FillEffectLine(__int64 panel, __int64 a2, __int64 a3, _WORD *layout)`
- **Callers:** Battle_UnitStatusFillAlt (layout mode 1)
- **Callees:** StatusList_BuildFromResultBlock, UnitPanel_SetSignalList, Status_PickHighestPriority, SceneObject_FindByUnitIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the effect line of the unit status panel (the panel beside the action preview and the AI's target panel) from the current target's result block: damage, recovery, a stat change, or the statuses the action would add or remove.

## Behavior

- V: reads the result block at qword_142FF3CF8 (the current target); flag byte +39: bit 0x80 HP damage (+6), 0x40 HP recovery (+8), 0x20 MP damage (+10), 0x10 MP recovery (+12), then the word +14 and the byte +42 with bit 0x01.
- V: with bit 0x08 it picks the top status (Status_PickHighestPriority), builds the status list (StatusList_BuildFromResultBlock into a 40-byte stack buffer) and hands it to UnitPanel_SetSignalList.
- V (traced live 2026-11-17): called while the action preview is up (a forecast pass) and on enemy turns (the target panel); not called when an action's result shows over the hit unit.

## State touched

- Calls: [StatusList_BuildFromResultBlock](StatusList_BuildFromResultBlock.md), [UnitPanel_SetSignalList](UnitPanel_SetSignalList.md), [SceneObject_FindByUnitIndex](SceneObject_FindByUnitIndex.md)

## Referenced by

- Called by: [Battle_UnitStatusFillAlt](Battle_UnitStatusFillAlt.md)
- Observed behaviours: [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md)

## Notes

Name is ours.

## Open questions

? the meaning of the word +14 and the byte +42 labels.
