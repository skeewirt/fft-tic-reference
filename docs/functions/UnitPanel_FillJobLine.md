# UnitPanel_FillJobLine

- **Address:** `0x14029B5CC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 UnitPanel_FillJobLine(int panel, _QWORD *nodes, unsigned int *rec, int *textKeys)`
- **Callers:** sub_140291490 (the unit panel fill; skipped for job id 28), sub_140295558
- **Callees:** JobTreePanel_SetJobIcon, UIText_Get, GUITextNode_SetTextExpandedTemp, sub_1400FE9D0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the job line of a unit panel from a 148-byte job record: the job icon, the job level, the JP and the JP to the next level.

## Behavior

- V: sets the job icon from rec +64 (JobTreePanel_SetJobIcon).
- V: the level node: when the level rec +68 is 0 or less it shows UI text 0x9D ("--"); otherwise the level as a number.
- V: the JP node (rec +76) and the next node (rec +80): UI text 0x50 ("--") when the level is 0 or less or the value is negative; otherwise the number.
- V: the fourth node (rec +84): also "--" when the level is 8 or more.
- V (seen live 2026-11-17): a monster unit (all job levels 0) shows "Lv. --" and "--" for JP and next.

## State touched

- Calls: [JobTreePanel_SetJobIcon](JobTreePanel_SetJobIcon.md), [UIText_Get](UIText_Get.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Referenced by

- Observed behaviours: [BattlePanelJobLineShowsDashesAtLevelZero](../behaviors/BattlePanelJobLineShowsDashesAtLevelZero.md)

## Notes

Name is ours. The record is the one JobRecord_FromJobId builds (BattleUnit_BuildJobRecord for the battle panels).

## Open questions

? the meaning of rec +80 versus rec +84 beyond "JP" and "next".
