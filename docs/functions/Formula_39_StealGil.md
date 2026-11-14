# Formula_39_StealGil

- **Address:** `0x140308098`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_39(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 39

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steal Gil: a physical evade check and a Speed-based hit, then a gil transfer.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 94 bytes.
- V: Typical abilities: Steal Gil, Glitterlust.
- V: The earlier sheet described a plain physical check; the hit chain is Speed + X.

## Calculation

```text
Physical evade check, then Speed + X through the magic chain
On success: transfers gil based on level, Speed and Y
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
