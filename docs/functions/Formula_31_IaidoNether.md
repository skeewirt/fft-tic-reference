# Formula_31_IaidoNether

- **Address:** `0x140307C28`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_31(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 31

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Iaido Nether: MA x Y with element, caster/Shell/Sleep/Zodiac and inverse-Faith scaling.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 294 bytes.
- V: Typical abilities: Hell's Wrath → Impiety.
- V: The earlier sheet described normal Faith scaling and no element boost; the current code uses element boost and inverse Faith.

## Calculation

```text
PA = MA
Y = (MA + ability_Y) / 2
Damage = MA × Y × [×5/4 element] × [×4/3 caster boost]
 × [×2/3 Shell] × [×3/2 Sleep] × Zodiac(50-150%)
 × [weather] × [element absorb/weak]
 × (100 - caster Faith) × (100 - target Faith) / 10000
capped at 32767, then counter + status
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
