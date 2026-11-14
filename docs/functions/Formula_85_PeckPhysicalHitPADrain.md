# Formula_85_PeckPhysicalHitPADrain

- **Address:** `0x140308FF8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_85(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 85

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Peck: a magic hit that reduces the target's PA.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 50 bytes.
- V: Typical abilities: Peck.
- V: The earlier sheet called this physical; the hit chain is magic.

## Calculation

```text
Magic hit check (MA + X chain)
On success: target PA reduced by Y & 0x7F
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
