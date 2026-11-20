# StatusVoice_SpeakEvent

- **Address:** `0x1401ECDB4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void StatusVoice_SpeakEvent(BattleVoiceController *c, const uint8_t *event)`
- **Callers:** sub_1401ECBBC
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Speaks the voice line of a status event: the line is read from the UIStatusEffect rows of every status in the event's mask and spoken only when the non-zero values agree.

## Behavior

- V: the event holds a 41-bit status mask (two qwords from +56; bit i selects the UIStatusEffect row of key i); returns at once when the mask is empty.
- V: for every set bit it reads the row's battle_voice column (+0x1C); non-zero values must all be equal, a differing value ends the function without speaking.
- V: with an agreed value v the controller's virtual slot 5 (IsSuppressed) is called with the event and v; when it answers 0 the virtual slot 3 (Speak) is called with v.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [sub_1401ECBBC](sub_1401ECBBC.md)
- Observed behaviours: [StatusSignalAndVoiceColumns](../behaviors/StatusSignalAndVoiceColumns.md)

## Notes

Name is ours (executable database: sub_1401ECDB4). The stock values are 15 for ailments and 23 for gains (M).

## Open questions

None recorded.
