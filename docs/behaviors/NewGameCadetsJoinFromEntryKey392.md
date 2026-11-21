# NewGameCadetsJoinFromEntryKey392

- **Kind:** observed behaviour
- **Scope:** engine (New Game party, chapter 1 opening)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [OverrideEntry_LoadBattleEntries](../functions/OverrideEntry_LoadBattleEntries.md), [Unit_ApplySpawnRecord](../functions/Unit_ApplySpawnRecord.md), [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [EventScript_Run](../functions/EventScript_Run.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The six level-1 units of a New Game party besides Ramza are not made by the party reset: they are entries 2..7 of entry key 392 (the unit list of events 7 and 8, map 24), each with bit 0x10 of entry +1, and the event script's opcode 0x43 mode 1 stores every battle unit carrying that bit into a free party save record. The OverrideEntryData rows (392, 2..7) are applied to those entries before the units are built, so their columns decide what joins.

## Behavior

- V (data): the scenario setup records of events 7 and 8 hold map 24 and entry key 392 (replay key 258); key 392 is block 8 of the fourth entry file (keys 384..511).
- V (data): entries 2..7 of key 392 are markers 0x80, 0x80, 0x80, 0x81, 0x81, 0x81 (generic male x3, female x3), level 1, jobs 74, 74, 75, 74, 74, 75 (Squire, Squire, Chemist each), name byte 255, entry +1 = 0x90 (male) / 0x50 (female): bit 0x10 set, bit 0x01 clear.
- V: Unit_ApplySpawnRecord copies the low five bits of entry +1 into work +6 (markers 0x80 / 0x81 replace only bits 0xE0) and sets work +2 = 0xFF, so bit 0x10 reaches the built unit.
- V: sub_140227458(arg) walks the 21 battle units; for a unit whose scene preview entry is its own index, whose work +6 has bit 0x10 and whose work +2 is 0xFF or whose marker is 1..3, and (arg is 0 or work +6 bit 0x01 is set), it calls sub_1402C8010 (sells equipment beyond the 99 cap) and UnitWork_StoreToSaveSlot, then sub_140279508 on the new save record.
- V: opcode 0x43 mode 1 calls sub_140227458 with a record byte while variable 39 is below 78 and with 0 from 78 on.
- I: this store is how the six units enter the party (the bit, the level-1 generics and the event fit; the call on events 7 and 8 was not caught).
- V (data): OverrideEntryData has stock rows (392, 1..7); rows 2..7 change nothing but the granted abilities (148, or 368 for entry 4, 381 for entry 7), so the job, sprite shape, name key, level, Brave, Faith, items, abilities and the remove byte of those rows apply to the six units before they are stored.
- ?: not seen live; the entry data was read from the shipped battle_entd files of pack 0002.

## Notes

Event numbers below 78 pass a non-zero argument when the record byte is non-zero, which limits the join to units with bit 0x01; the six entries have it clear, so they join only when the argument is 0.

## Open questions

? which record byte the mode 1 call passes on events 7 and 8 (offset 171 or 91 of the record at qword_143CD9DE0); ? whether a marker other than 0x80 / 0x81 (a sprite shape set by the row) still joins as a normal party unit.
