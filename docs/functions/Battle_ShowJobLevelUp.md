# Battle_ShowJobLevelUp

- **Address:** `0x1402041D8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 Battle_ShowJobLevelUp(__int64 task)`
- **Callers:** sub_14020435C, sub_140205F28
- **Callees:** BattleMsg_Dispatch, sub_140269AAC, sub_1401FA7D4, sub_1401FAE5C, sub_1401D964C, sub_1401FF578, sub_1400D6DAC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows the job level-up banner over the acting unit when its action raised its job level.

## Behavior

- V: returns 0 when the task byte +465 (the new job level from Battle_ActorResultLevels) is 0.
- V: otherwise sets word_1408080EC to 180, dispatches battle message 6206 for the unit (BattleMsg_Dispatch(10, 6206, unit index, unit index, 1, 0)), plays sound effect 7 and starts the banner motion; returns 1.
- V (seen live 2026-11-17): the banner reads "<unit>'s <job> job level increased!".
- I: its text is C_Mes_Id_Sample 3062 (the only text with that wording), whose job name comes from the unit's job byte (BattleMsg_BuildArgs).

## State touched

- Calls: [BattleMsg_Dispatch](BattleMsg_Dispatch.md)

## Notes

Name is ours. Message 6207 is the unit level-up twin (Battle_ShowUnitLevelUp).

## Open questions

? how message 6206 of the dispatch leads to text 3062.
