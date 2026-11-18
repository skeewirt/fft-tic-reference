# Battle_GetEntryBlock

- **Address:** `0x14028416C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `uint8_t *Battle_GetEntryBlock(void)`
- **Callers:** Battle_BuildEntryUnits, sub_1402841D0
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The 16 spawn entries (40 bytes each, 640 bytes) of the current battle inside the loaded entry data.

## Behavior

- V: returns null when the key dword of g_BattleEntrySource is 0 or the dword at 0x141856AB4 is not 0.
- V: otherwise the entry base pointer (g_BattleEntrySource +8) + 640 x n, where n is the key minus 512 for keys of 512 or more, else the key reduced below 128 (minus 128, 256 or 384).

## State touched

- Reads: [g_BattleEntrySource](../globals/g_BattleEntrySource.md)

## Referenced by

- Appears in flows: [ScriptedBattleUnitsFromEntries](../flows/ScriptedBattleUnitsFromEntries.md)
- Called by: [Battle_BuildEntryUnits](Battle_BuildEntryUnits.md)
- Observed behaviours: [BattleEntryDataIsFiveFilesByKey](../behaviors/BattleEntryDataIsFiveFilesByKey.md)

## Notes

I: the entry data is the battle placement data (ENTD in the original game) loaded behind g_BattleEntrySource +8; its file and loader were not traced.

## Open questions

? what the dword at 0x141856AB4 means.
