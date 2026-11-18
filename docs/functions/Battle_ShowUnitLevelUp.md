# Battle_ShowUnitLevelUp

- **Address:** `0x14020401C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 Battle_ShowUnitLevelUp(__int64 task)`
- **Callers:** sub_14020435C, sub_140205F28
- **Callees:** BattleMsg_Dispatch, sub_140269AAC, sub_1401FA7D4, sub_1401FAE5C, sub_1401D964C, sub_1400DF354, sub_1401FF578, sub_1400D6DAC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows the level-up banner over the acting unit when its action raised its unit level.

## Behavior

- V: returns 0 when the task byte +464 (the new unit level from Battle_ActorResultLevels) is 0.
- V: otherwise sets word_1408080EC to 180, dispatches battle message 6207 for the unit, plays sound effect 3, starts the banner motion and posts a LevelUpNotification with the unit byte +0 and the level +41; returns 1.

## State touched

- Calls: [BattleMsg_Dispatch](BattleMsg_Dispatch.md)

## Notes

Name is ours.

## Open questions

None recorded.
