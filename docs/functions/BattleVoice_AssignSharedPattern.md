# BattleVoice_AssignSharedPattern

- **Address:** `0x1401ED240`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_AssignSharedPattern(void *battleControl, int slot, int pattern)`
- **Callers:** sub_1401EDB88
- **Callees:** sub_1401EC530

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the pattern of one shared voice controller.

## Behavior

- V: calls BattleVoice_SetPattern for the shared controller (BattleControl +689112 + 136 * slot).

## Notes

Name is ours.

## Open questions

None recorded.
