# FormulaIdsPastTheByte

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Ability data](../areas/ability-data.md)
- **Affects:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Formula_106_ReDispatchChainFormula](../functions/Formula_106_ReDispatchChainFormula.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every hop of a formula id is one byte and the registry has 106 rows; the clamp `(u8)(id - 1) > 0x69 -> 1` sends any other value to formula 1.

## Behavior

- V (code): sources are the action record +8, the weapon record +2, the chemist record +0 (the formula block's +8 ability word and +0x0A item word name them); the clamp `(u8)(id - 1) > 0x69 -> 1` at 0x140309DAC; one dispatch at 0x140309F53; Formula_106 re-dispatches the weapon byte unclamped; ten readers of block +0x18 test stock formula ids (none names 255).

## Open questions

? formula ids past 106 skip the per-formula Undead hooks.
