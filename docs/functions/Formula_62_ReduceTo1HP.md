# Formula_62_ReduceTo1HP

- **Address:** `0x140308A44`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_62(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 62

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reduce to 1 HP: sets the target's HP to 1 with no hit check or modifiers.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 43 bytes.

## Calculation

```text
Damage = target_CurHP - 1 (always reduces to exactly 1 HP)
No hit check, no modifiers, always succeeds
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
