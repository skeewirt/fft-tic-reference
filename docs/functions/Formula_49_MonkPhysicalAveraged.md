# Formula_49_MonkPhysicalAveraged

- **Address:** `0x1403086F4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_49(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 49

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Monk physical (averaged): PA x Y where Y is averaged with PA, then the physical chain.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 139 bytes.
- V: Typical abilities: Cyclone, Aurablast, Shockwave.

## Calculation

```text
PA = caster PA stat, Y = (ability_Y + PA) / 2
Damage = PA × Y × [×5/4 element] × [×3/2 Berserk]
 × [×2/3 target Protect] × [×3/2 target Sleep]
 × Zodiac(50-150%) × [critical] × [weather] × [element absorb/weak]
capped at 32767, then counter + status check
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
