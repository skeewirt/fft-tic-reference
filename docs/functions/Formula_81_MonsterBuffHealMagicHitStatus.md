# Formula_81_MonsterBuffHealMagicHitStatus

- **Address:** `0x140308E90`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_81(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 81

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Monster buff/heal: a magic hit check that applies a status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 83 bytes.
- V: Typical abilities: Choco Esuna, Guardian Nymph, Shell Nymph.

## Calculation

```text
Hit = (MA + X) × [×5/4 element] × [×4/3 MagicAttackUp]
    × Zodiac(50-150%) × faith_scaling
On success: apply status via F56 engine
(Uses CalcTotalDamage — additive base, same as F10/F11)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
