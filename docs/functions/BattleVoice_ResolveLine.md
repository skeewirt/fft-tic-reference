# BattleVoice_ResolveLine

- **Address:** `0x1401ECF84`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleVoice_ResolveLine(void *controller, int line)`
- **Callers:** sub_1401EC958
- **Callees:** NxdEntry_GetRow, NxdRegistry_Find, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves a BattleVoice line to the cue number to play, with the three replacement rules.

## Behavior

- V: returns the row's cue (+8), or the cue of a replacement row: battle_voice (+0x10) when controller flag bit 0 is set (the speaker's VoicePattern flag), battle_voice_2 (+0x14) when bit 1 is set (patterns 100 / 101), battle_voice_3 (+0x18) when the controller's pattern id (+12) is 63.

## State touched

- Calls: [NxdEntry_GetRow](NxdEntry_GetRow.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)

## Notes

Name is ours.

## Open questions

None recorded.
