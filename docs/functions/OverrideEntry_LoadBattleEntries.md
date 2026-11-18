# OverrideEntry_LoadBattleEntries

- **Address:** `0x1401EA574`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void OverrideEntry_LoadBattleEntries(unsigned int key, uint8_t *entries, int *extra, const char **rows)`
- **Callers:** Battle_BuildEntryUnits
- **Callees:** sub_1403D325C, sub_1403D3B5C (row by two keys), sub_1403D2FD8, OverrideEntry_FillUnitEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fetches the 16 pre-placed unit entries of one scripted battle from OverrideEntryData (nxd table 96) and converts each row into a 40-byte unit entry.

## Behavior

- V: looks up nxd table 96 (cached in a global after the first lookup).
- V: for index 0..15 asks the table for the row with the pair (key, index); the lookup is by two keys, not by row position.
- V: when a row exists, stores its pointer in the caller's row array and calls sub_1401EA638 to fill the 40-byte entry for that index; absent rows leave the entry untouched.
- V: advances the output entry pointer by 40 bytes and the second output by 4 bytes per index.
- V: its caller Battle_BuildEntryUnits passes the battle's entry block itself (Battle_GetEntryBlock), so the rows overwrite the loaded entries in place, and hands the row array on to Battle_PlaceEntryUnits, which gives row i to Unit_BuildFromRecord as its fifth argument for battle unit i.

## State touched

- Calls: [OverrideEntry_FillUnitEntry](OverrideEntry_FillUnitEntry.md)

## Referenced by

- Appears in flows: [ScriptedBattleUnitsFromEntries](../flows/ScriptedBattleUnitsFromEntries.md)
- Called by: [Battle_BuildEntryUnits](Battle_BuildEntryUnits.md)
- Observed behaviours: [BattleEntryDataIsFiveFilesByKey](../behaviors/BattleEntryDataIsFiveFilesByKey.md), [SpawnedUnitsCarryAOneByteJob](../behaviors/SpawnedUnitsCarryAOneByteJob.md)
- Reads tables: [NxdDataOverrideEntryData](../tables/NxdDataOverrideEntryData.md)

## Notes

The table holds 516 rows in the shipped data, which is 16 slots for each scripted battle. Battle_BuildEntryUnits tests the dword at 0x1407D453C.

## Open questions

Whether the script runner calls this path as well; only Battle_BuildEntryUnits appears as a direct caller.
