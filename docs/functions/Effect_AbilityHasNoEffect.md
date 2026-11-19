# Effect_AbilityHasNoEffect

- **Address:** `0x140319D74`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Effect_AbilityHasNoEffect(int effectWord)`
- **Callers:** BattleAct_Step, sub_14020CC50, sub_140210AF0, sub_14026A508
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when an effect word has no effect file (g_AbilityEffectNumber < 0), except 146 and 405..413.

## Behavior

- V: (word - 405) > 8 && word != 146 && g_AbilityEffectNumber[word] < 0; no bound on the word (an id past 453 reads the next table).

## Referenced by

- Called by: [BattleAct_Step](BattleAct_Step.md), [sub_14020CC50](sub_14020CC50.md), [sub_14026A508](sub_14026A508.md)

## Open questions

None recorded.
