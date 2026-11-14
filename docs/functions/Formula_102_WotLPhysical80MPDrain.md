# Formula_102_WotLPhysical80MPDrain

- **Address:** `0x14030D5AC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_102(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 102

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

WotL physical: PA x WP damage reduced to 80%, with the difference restoring the caster's MP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 107 bytes.
- V: The earlier sheet said HP drain; the current code drains MP.

## Calculation

```text
Physical evade check
Damage = PA × WP through the physical chain
Damage = 80% of the result
Caster recovers MP equal to the damage dealt
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

Which ability uses this formula.
