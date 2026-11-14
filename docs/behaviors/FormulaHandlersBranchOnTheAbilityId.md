# FormulaHandlersBranchOnTheAbilityId

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Ability data](../areas/ability-data.md)
- **Affects:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Formula_42_Speechcraft](../functions/Formula_42_Speechcraft.md), [Formula_28_BardSongs](../functions/Formula_28_BardSongs.md), [Formula_29_DancerDances](../functions/Formula_29_DancerDances.md), [Action_PickTargetEquipment](../functions/Action_PickTargetEquipment.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle_ResolveAction reads one formula id per action (a byte), clamps it and calls one registry handler; many handlers then branch on the id of the ability being resolved (the formula block's +8 word).

## Behavior

- V (code): the formula comes from the action record +8 (command kinds 0, 3, 6, 7 and 4), the weapon record +2 (kinds 8, 10), the chemist record +0 (kind 1) or a constant (99, 100, 1); it is clamped ((u8)(id - 1) > 0x69 -> 1), stored once at g_FormulaBlock +0x18 and dispatched once at 0x140309F53; every hop is one byte. Formula_106 re-dispatches with the weapon's byte, unclamped.
- V (code): the formula block +8 (0x1407B0778) holds the ability being resolved; the songs (28: 86..92), dances (29: 93..99), talk skills (42: 117..121, 123), equipment picks (37, 38, 46: 18 ids), formulas 26 / 43 (143..145, 197..199) and the shared helpers testing ability 0, 65 and 219 read it. Formula 4 writes it (the weapon's spell).
- V (code): a 106-row per-formula hook table (PostBattleCalc, Battle_Init) gives 12 formulas an Undead rule; formula ids above 106 skip it, and ten readers of +0x18 test stock formula ids (7, 42, 99, 106, sets of 21 and 45 ids).

## Open questions

? the 357 / 358 inflict tests before the dispatch read the own id.
