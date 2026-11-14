# Formula_51_Purification

- **Address:** `0x140308820`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_51(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 51

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Purification: an additive PA + X hit check that removes negative statuses.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 83 bytes.
- V: Typical abilities: Purification.

## Calculation

```text
Hit = (PA + X) × [×3/2 Berserk] × [×3/2 Charging]
 × Zodiac(50-150%) × faith_scaling
On success: removes negative statuses from target
(ADDITIVE base)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
