# Formula_59_Shout

- **Address:** `0x140306074`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_59(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 59

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shout: a self-only combined Brave/PA/MA/Speed increase.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 40 bytes.
- V: Typical abilities: Shout.

## Calculation

```text
Self only: Brave += X, PA += Y, MA += Y, Speed += Y
(always succeeds, all stats boosted at once)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
