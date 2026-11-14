# Formula_34_DrawOutBuff

- **Address:** `0x140307DE8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_34(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 34

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw Out buff: status-only; applies the buff carried by the ability data.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 18 bytes.
- V: Typical abilities: Kiyomori (→Protect+Shell), Masamune (→Regen+Haste).

## Calculation

```text
Status-only: applies buff from ability data (no damage)
Uses F56 status engine for Protect, Shell, Regen, Haste etc
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
