# Formula_57_Tailwind

- **Address:** `0x14030605C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_57(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 57

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tailwind: a self-only Speed increase that always succeeds.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 24 bytes.
- V: Typical abilities: Tailwind.

## Calculation

```text
Self only: Speed += Y (always succeeds, no calculation)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
