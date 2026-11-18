# BattleUnitOnFieldByte

- **Kind:** observed behaviour
- **Scope:** battle unit +0x1B5
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_BuildRosterTeam](../functions/Battle_BuildRosterTeam.md), [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle unit byte +0x1B5 (437): 1 placed on the field, 0 not placed (benched), 0xFF an empty slot.

## Behavior

- V: written by Battle_BuildRosterTeam and Battle_PlaceEntryUnits.
- V (seen live 2026-11-13): in a resumed battle the empty slots 9..15 and the benched chocobo and red panther all named look pool record 0.

## Open questions

None recorded.
