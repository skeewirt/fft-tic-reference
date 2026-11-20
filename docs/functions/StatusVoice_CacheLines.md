# StatusVoice_CacheLines

- **Address:** `0x1401EB468`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void StatusVoice_CacheLines(BattleControl *bc)`
- **Callers:** Battle_Init
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the battle_voice column of UIStatusEffect rows 1..40 into an array of 40 dwords in the battle control at +693504.

## Behavior

- V: for key 1..40 stores the row's dword +0x1C (0 when the row is missing) at BattleControl +693504 + 4 * (key - 1).
- V: called from Battle_Init once per battle.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Observed behaviours: [StatusSignalAndVoiceColumns](../behaviors/StatusSignalAndVoiceColumns.md)

## Notes

Name is ours (executable database: sub_1401EB468).

## Open questions

? no reader of the cached array was found: StatusVoice_SpeakEvent reads the table rows itself.
