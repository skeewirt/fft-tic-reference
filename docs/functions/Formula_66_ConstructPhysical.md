# Formula_66_ConstructPhysical

- **Address:** `0x140308B7C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_66(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 66

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Construct physical: a primary PA x Y hit plus a secondary PA x Y / X hit.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 111 bytes.
- V: Typical abilities: Destroy, Compress, Dispose, Pulverize.

## Calculation

```text
Primary: Damage = PA × Y × Zodiac(50-150%)
Secondary: Damage = PA × Y / X
(two hits, no other modifiers)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
