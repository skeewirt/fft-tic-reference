# Battle_BuildEntryUnits

- **Address:** `0x14030428C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Battle_BuildEntryUnits(void)`
- **Callers:** sub_1403044EC (battle load state 5, after state 4 set the key from scene variable 50), sub_14030476C
- **Callees:** Battle_GetEntryBlock, OverrideEntry_LoadBattleEntries, Battle_PlaceEntryUnits, sub_1402F3A04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the battle units of the current battle from its 16 entries: fetches the entry block, lets the battle's OverrideEntryData rows overwrite the entries, then places the units.

## Behavior

- V: entries = Battle_GetEntryBlock(); nothing happens (returns 0) when that is null.
- V: zeroes a 64-byte array (one dword per entry) and an array of 16 row pointers on its stack.
- V: when the dword at 0x1407D453C is not 0: OverrideEntry_LoadBattleEntries(g_BattleEntrySource key dword, entries, dwords, rows), which fills the entry block in place.
- V: then Battle_PlaceEntryUnits(entries, ?, dwords, rows) and sub_1402F3A04(g_BattleEntrySource +8, the entry base pointer); returns 0.

## State touched

- Calls: [Battle_GetEntryBlock](Battle_GetEntryBlock.md), [OverrideEntry_LoadBattleEntries](OverrideEntry_LoadBattleEntries.md), [Battle_PlaceEntryUnits](Battle_PlaceEntryUnits.md)
- Reads: [g_BattleEntrySource](../globals/g_BattleEntrySource.md)

## Notes

Replaces the older reference sheet sub_14030428C, which named OverrideEntry_LoadBattleEntries as the first call and a language id as its argument; the first call is Battle_GetEntryBlock and the argument is the battle key.

## Open questions

? what sub_1402F3A04 does with the entry base pointer; ? the second argument of Battle_PlaceEntryUnits (rdx is not set here).
