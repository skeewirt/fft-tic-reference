# BattleLabel_ShowReactionSignal

- **Address:** `0x14014BFFC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleLabel_ShowReactionSignal(__int64 screen, int slot, unsigned int signal, int raised)`
- **Callers:** ResultLabel_ShowNext
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a plain text label (a BattleSignal title) over a unit, in the TextReaction node.

## Behavior

- V: does nothing for a slot above 20 or without the node at screen +144 * slot + 88; looks up the BattleSignal row signal.
- V: positions the node at (-80, 28) when the fourth argument is non-zero, else (-80, 80), and fills the TextReaction part.
- V (traced live 2026-11-17): called with slot 17 and signal 62 (Shield parry!) when a unit blocked a hit.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Called by: [ResultLabel_ShowNext](ResultLabel_ShowNext.md)

## Notes

Name is ours.

## Open questions

None recorded.
