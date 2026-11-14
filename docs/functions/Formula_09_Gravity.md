# Formula_09_Gravity

- **Address:** `0x140307474`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_09(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 9

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gravity damage: a percentage of the target's maximum HP, gated by a magic hit check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 117 bytes.
- V: Typical abilities: Gravity, Graviga, Lich.

## Calculation

```text
Damage = (Y × target_MaxHP + 99) / 100
Hit check: (MA + X) × [×4/3 MagicAttackUp] × [×2/3 Shell] × [×3/2 Sleep]
 × Zodiac(50-150%) × Faith(caster×target/10000)
 must pass for damage to apply
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
