# Formula_76_MagicHealSimplified

- **Address:** `0x140308D0C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_76(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 76

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic heal (simplified): MA x Y healing with caster boost and Zodiac, then the undead check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 60 bytes.
- V: Typical abilities: Choco Cure, Life Nymph.

## Calculation

```text
Heal = MA × Y × [×4/3 caster boost] × Zodiac(50-150%)
capped at 32767, then Undead reverse check
(no faith scaling, no element boost, no Shell)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
