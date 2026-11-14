# Formula_78_MAYPhysicalFullChain

- **Address:** `0x140308DBC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_78(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 78

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MA x Y physical: the full magic chain applied to a physical-style attack.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 55 bytes.
- V: Typical abilities: Breath attacks, Cloud limits (Braver→Omnislash), monster attacks (25 total).

## Calculation

```text
Damage = MA × Y × [×5/4 element] × [×4/3 caster boost]
 × [×2/3 Shell] × [×3/2 Sleep] × Zodiac(50-150%)
 × [weather] × [element absorb/weak]
capped at 32767, then counter + status check
(MULTIPLICATIVE, uses MA not PA)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
