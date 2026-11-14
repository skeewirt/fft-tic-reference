# BattleLoadWritesThePartyBackToTheSaveRecords

- **Kind:** observed behaviour
- **Scope:** loading a story battle from the world map
- **Area:** [Save data](../areas/save-data.md)
- **Affects:** [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

While a battle loads, the game writes every party work record back into its save record (PartyUnit_WriteBackToSave once per party slot, 0 to 6 with a party of seven).

## Behavior

- V: seen live 2026-11-09 (Mandalia Plain from the world map, debugger tracepoint on PartyUnit_WriteBackToSave): seven calls with the party index 0..6 in the first argument, all from one thread in one frame, before the deployment screen.
- ?: which caller of PartyUnit_WriteBackToSave runs at the battle load (ten callers listed on its sheet).

## Open questions

? The caller at the battle load; ? whether other scene changes (town entry, formation) run the same write-back.
