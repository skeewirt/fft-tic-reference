# Formula_33_DrawOutDamageStatus

- **Address:** `0x140307D84`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_33(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 33

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw Out damage plus status: MA x Y magic damage written to the MP-damage field.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 98 bytes.
- V: Typical abilities: Bizen Osafune.
- V: The earlier sheet described HP damage; the current code writes MP damage.

## Calculation

```text
MA = caster MA, Y = ability_Y
MP damage = MA × Y × [×4/3 caster boost] × [×2/3 Shell]
 × [×3/2 Sleep] × Zodiac(50-150%)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
