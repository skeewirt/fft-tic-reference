# Formula_30_IaidoHeaven

- **Address:** `0x140307C10`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_30(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 30

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Iaido Heaven: PA is replaced by MA and Y is averaged with MA, then the magic chain runs.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 23 bytes.
- V: Typical abilities: Heaven's Wrath → Divinity, Holy Breath.
- V: F30, F94 and F95 resolve to the same function in the current build.

## Calculation

```text
PA = MA, Y = (MA + ability_Y) / 2
Damage = PA × Y × [×5/4 element] × [×4/3 caster boost]
 × [×2/3 Shell] × [×3/2 Sleep] × Zodiac(50-150%)
 × [weather] × [element absorb/weak]
capped at 32767, then counter + status check
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
