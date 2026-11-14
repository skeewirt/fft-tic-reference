# Formula_64_SealEvil

- **Address:** `0x140308ABC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_64(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 64

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Seal Evil: a Speed-based hit check that only affects undead targets.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 102 bytes.
- V: Typical abilities: Seal Evil.

## Calculation

```text
Hit = (Speed + X) × [phys modifiers] × Zodiac × faith_scaling
On success: applies status ONLY if target is Undead
(ADDITIVE, uses SPEED. Fails on non-Undead targets)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
