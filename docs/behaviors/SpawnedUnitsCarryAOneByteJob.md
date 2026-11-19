# SpawnedUnitsCarryAOneByteJob

- **Kind:** observed behaviour
- **Scope:** engine (spawn records, scripted battle entries)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [UnitWork_InitFromSpawnRecord](../functions/UnitWork_InitFromSpawnRecord.md), [OverrideEntry_FillUnitEntry](../functions/OverrideEntry_FillUnitEntry.md), [OverrideEntry_LoadBattleEntries](../functions/OverrideEntry_LoadBattleEntries.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A spawned unit's job is one byte of its spawn record (+10), copied into the work record's job byte; the scripted-battle table OverrideEntryData has a 32-bit job column, but the copy keeps only its low byte. The engine keeps the job in one byte there, so it cannot carry a job id above 255 to a spawned unit.

## Behavior

- V (disassembly): UnitWork_InitFromSpawnRecord loads the spawn record's byte +10 (0x140276B04) into the work record's job byte C +3 (0x140276B07) and then calls UnitWork_ApplyJobRow.
- V (decompile): OverrideEntry_FillUnitEntry stores row dword +0x10 (job), when it is not 0, as one byte into its 40-byte unit entry at +10: 300 becomes 44.
- V (disassembly): Unit_ApplySpawnRecord writes 0xFF into C +2 on one of its branches (0x1402763FB); C +2 is the save index (54 entries).
- V (2026-11-09): the 40-byte unit entries of OverrideEntry_LoadBattleEntries are spawn records: Battle_BuildEntryUnits passes the battle's entry block (Battle_GetEntryBlock) to it, so the rows overwrite the entries in place, and Battle_PlaceEntryUnits builds battle unit i from entry i with Unit_BuildFromRecord, giving it row i as the fifth argument (flow ScriptedBattleUnitsFromEntries).

## Notes

Stock rows of OverrideEntryData use job values 2, 154 and 169..173 (checked against every stock row), all below 256, so the byte cast changes no stock unit.

## Open questions

? whether an event command can change a spawned unit's job (no opcode that carries a job id was found).
