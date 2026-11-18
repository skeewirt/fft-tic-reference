# Battle_PlaceEntryUnits

- **Address:** `0x14027128C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Battle_PlaceEntryUnits(uint8_t *entries, ?, uint32_t *dwords, const uint8_t **rows)`
- **Callers:** Battle_BuildEntryUnits
- **Callees:** Unit_BuildFromRecord, Unit_ResolvePreviewShape, sub_140278E0C, sub_140271178, sub_140271844, LookQueue_Add, SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds battle unit i (g_PreviewUnitTable + 512 x i) from entry i for the 16 entries of a battle, decides who is placed and queues each placed unit's look.

## Behavior

- V: first stores into byte_140D405AB the highest byte +29 of the save records in use (+1 not 0xFF), capped at 99 (Unit_ApplySpawnRecord bases random and relative levels on it).
- V: for i = 0..15: unit +444 = i, unit +504 = dwords[i], g_CurrentSpawnEntry = entry i; an entry whose byte 0 is 0 leaves the unit empty (+1 and +437 = 0xFF).
- V: otherwise +1 = i, +437 = 1 and Unit_BuildFromRecord(unit, entry, 0, 0, rows ? rows[i] : null): the entry's OverrideEntryData row is the fifth argument.
- V: then the shape (Unit_ResolvePreviewShape) goes to +399, the palette to +400, +401 is the entry's byte +32 unless 0xFF (else a counter from 0xFE down), and the entry's bytes +25..+27, +30, +31 give +79..+81, +404 and +406.
- V: team bits +5 & 0xC0 and sub_140271178 / sub_140271844 decide whether the unit is kept; a kept unit is queued with LookQueue_Add (sprite 27 becomes 36 when scene variable 39 is 388 and +444 is 1).

## State touched

- Calls: [Unit_BuildFromRecord](Unit_BuildFromRecord.md), [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md), [LookQueue_Add](LookQueue_Add.md), [SceneVar_Read](SceneVar_Read.md)
- Writes: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md), [g_CurrentSpawnEntry](../globals/g_CurrentSpawnEntry.md)

## Referenced by

- Appears in flows: [ScriptedBattleUnitsFromEntries](../flows/ScriptedBattleUnitsFromEntries.md)
- Called by: [Battle_BuildEntryUnits](Battle_BuildEntryUnits.md)
- Observed behaviours: [BattleUnitOnFieldByte](../behaviors/BattleUnitOnFieldByte.md), [BattleUnitTableListsEnemyRowsThatAreNotOnTheField](../behaviors/BattleUnitTableListsEnemyRowsThatAreNotOnTheField.md)

## Notes

So battle slot i is always built from entry i, and its OverrideEntryData row is the same row index i of the battle key. The count of kept units is limited by scene variable 57 (7 + 9 - value).

## Open questions

? the exact placement rules of sub_140271178 and sub_140271844 (not read).
