# Formula_97_MagicBasedBraveModify

- **Address:** `0x140309318`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_97(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 97

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic-based Brave modify: a magic hit check that adjusts the target's Brave.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 50 bytes.
- V: Typical abilities: Trepidation, Chicken.

## Calculation

```text
Hit check: magic chain (MA + X) × all magic modifiers × Faith²/10000
On success: target's Brave adjusted by Y & 0x7F
(uses MAGIC hit check, faith-dependent)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

Why F98 is labelled physical-based while using the single-faith magic chain.
