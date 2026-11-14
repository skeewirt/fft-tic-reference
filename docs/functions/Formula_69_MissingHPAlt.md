# Formula_69_MissingHPAlt

- **Address:** `0x140306114`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_69(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 69

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Missing HP (alternate): uses the target's missing HP, with no hit check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 31 bytes.
- V: The earlier sheet called this identical to F67; the current code uses the target's missing HP.

## Calculation

```text
Damage = target MaxHP - target current HP
No hit check
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
