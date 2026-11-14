# Formula_58_Steel

- **Address:** `0x140306044`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_58(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 58

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steel: a self-only Brave increase that always succeeds.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 24 bytes.
- V: Typical abilities: Steel.

## Calculation

```text
Self only: Brave += Y (always succeeds, no calculation)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
