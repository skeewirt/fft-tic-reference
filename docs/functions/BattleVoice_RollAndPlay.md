# BattleVoice_RollAndPlay

- **Address:** `0x1401EC958`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_RollAndPlay(void *controller, void *request, int line)`
- **Callers:** sub_1401ED3A0
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, GlobalWork_GetFastForwardMode, sub_1401ED12C, sub_1401E8AF4, sub_1401ECF84, sub_14008FC68, sub_14009C034

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rolls the play chance of a voice line and plays it at once or queues it with its delay.

## Behavior

- V: does nothing while the GlobalWork fast-forward mode (+88) is 1 or 2.
- V: rolls a random number below 100 against the group chance (BattleVoiceGroupRate_Chance) and continues only when the roll is below it.
- V: the cue is the id from BattleVoice_ResolveLine; with a delay (+0x1C) above about 0 it is queued with the delay on the controller's queue, otherwise it plays at once through sub_14009C034.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md)
- Reads: [BattleVoiceController.group_key](../structs/BattleVoiceController.md#group_key)
- Writes: [BattleVoiceController.cue_queue](../structs/BattleVoiceController.md#cue_queue)

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)
- Observed behaviours: [BattleVoiceChance](../behaviors/BattleVoiceChance.md)

## Notes

Name is ours.

## Open questions

None recorded.
