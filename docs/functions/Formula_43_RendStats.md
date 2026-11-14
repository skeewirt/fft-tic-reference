# Formula_43_RendStats

- **Address:** `0x1403083F4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_43(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 43

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rend stats: physical damage then a PA/MA/Speed reduction based on the ability.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 82 bytes.
- V: Typical abilities: Rend Speed, Rend Power, Rend Magick.
- V: The earlier sheet used MA; the current code uses PA and the physical chain.

## Calculation

```text
Physical evade check
Damage = PA × Y × [×4/3 caster boost] × [×2/3 Shell]
 × [×3/2 Sleep] × Zodiac(50-150%)
then stat reduction (PA/MA/Speed based on ability)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
