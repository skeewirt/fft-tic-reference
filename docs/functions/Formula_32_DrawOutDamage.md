# Formula_32_DrawOutDamage

- **Address:** `0x140307D50`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_32(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 32

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw Out damage: MA x Y through the magic chain, with weather and element checks.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 50 bytes.
- V: Typical abilities: Ashura, Kotetsu, Muramasa, Chirijiraden.
- V: The earlier sheet called this a physical chain; it is the magic chain.

## Calculation

```text
MA = caster MA, Y = ability_Y
Damage = MA × Y × [×5/4 element] × [×4/3 caster boost]
 × [×2/3 Shell] × [×3/2 Sleep] × Zodiac(50-150%)
 × [weather] × [element absorb/weak]
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
