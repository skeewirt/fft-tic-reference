# BattleVoice_SetPattern

- **Address:** `0x1401EC530`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_SetPattern(void *controller, int pattern)`
- **Callers:** sub_1401ED240
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_140037CA4, Resource_FindOrOpen

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives a voice controller its voice pattern: group key, flags and voice bank.

## Behavior

- V: controller +12 = the pattern id; controller +8 bit 0 = the pattern row's flag byte (+0x14); bit 1 set for patterns 100 and 101; controller +16 = the pattern row's group key (+0xC, a BattleVoiceGroupRate key).
- V: controller +24 = the voice bank resource opened from the pattern row's path (+8).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [Resource_FindOrOpen](Resource_FindOrOpen.md)
- Writes: [BattleVoiceController.pattern_id](../structs/BattleVoiceController.md#pattern_id), [BattleVoiceController.pattern_flags](../structs/BattleVoiceController.md#pattern_flags), [BattleVoiceController.group_key](../structs/BattleVoiceController.md#group_key), [BattleVoiceController.voice_bank](../structs/BattleVoiceController.md#voice_bank)

## Notes

Name is ours.

## Open questions

None recorded.
