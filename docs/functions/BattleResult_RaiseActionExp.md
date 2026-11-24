# BattleResult_RaiseActionExp

- **Address:** `0x14030C110`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleResult_RaiseActionExp(int targetChanged)`
- **Callers:** Battle_ApplyActionResult
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the EXP the acting unit earns for the action in play, from one target: the level difference plus a base, kept only when it is larger than what an earlier target gave.

## Behavior

- V: does nothing when the argument is 0, when g_BattleStateGate is not 0 or when there is no caster unit.
- V: base 10 for the argument 1; else 20, divided by the target's KO count (unit +0x18C) when that is not 0.
- V: EXP = target level - caster level + base (levels at unit +0x29), at least 1; doubled when the caster's byte +0x99 has 0x20; at most 99.
- V: the global byte 0x1407B078A keeps the larger of its value and that EXP. Battle_AwardUnitJp adds the byte to the unit's EXP and gives JP only when it is not 0.
- V: two callers, both in Battle_ApplyActionResult: with 2 after a target went to KO (0x14030A8FB), and with the 'target changed' flag at the end of the status step (0x14030AA58).

## Referenced by

- Observed behaviours: [AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget](../behaviors/AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget.md)

## Notes

The name is ours (IDB: sub_14030C110). Behaviour record: AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget.

## Open questions

? who clears the EXP byte between actions.
