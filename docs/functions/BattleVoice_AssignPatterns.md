# BattleVoice_AssignPatterns

- **Address:** `0x1401EDB88`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_AssignPatterns(void *battleControl, void *unit)`
- **Callers:** Battle_RebuildUnitInPlace, sub_1401EA4D8, sub_140214610
- **Callees:** sub_1401EDD50, sub_1401ED240

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives a battle unit's voice controller its pattern, from the unit's job and name key.

## Behavior

- V: the pattern id comes from Unit_GetVoicePatternId(job byte +3, name key +508, ...).
- V: units whose byte +6 has bit 7 or bit 6 also use the shared controllers with patterns 100 or 101 (sub_1401ED240); patterns 102 and 103 are two more shared controllers (BattleControl +693224 and +693304).

## Referenced by

- Called by: [sub_140214610](sub_140214610.md)

## Notes

Name is ours.

## Open questions

None recorded.
