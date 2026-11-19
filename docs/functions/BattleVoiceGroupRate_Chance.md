# BattleVoiceGroupRate_Chance

- **Address:** `0x1401ED12C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleVoiceGroupRate_Chance(void *controller, int line)`
- **Callers:** sub_1401EC958
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the play chance in percent of a voice line for the speaker's group.

## Behavior

- V: takes the BattleVoiceGroupRate row of the controller's group key (+16) and the dword at +8 + 4 * k, where k is the line's chance_column (BattleVoice +0xC), when k is below 50; the result is capped at 100.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)
- Observed behaviours: [BattleVoiceChance](../behaviors/BattleVoiceChance.md)

## Notes

Name is ours. Only +8 + 4k of the row is ever read.

## Open questions

None recorded.
