# Formula_55_RushBasicPhysical

- **Address:** `0x14030895C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_55(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 55

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rush/basic physical: PA x a random number of hits with the standard physical modifiers.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 198 bytes.
- V: Typical abilities: Rush, Throw Stone, Cat Scratch, Tail Sweep.

## Calculation

```text
Hits = random(1..Y)
Damage = PA × Hits × [×3/2 Berserk] × [×2/3 target Protect]
 × [×3/2 Sleep] × Zodiac(50-150%)
+ random critical hit chance
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
