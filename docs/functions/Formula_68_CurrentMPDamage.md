# Formula_68_CurrentMPDamage

- **Address:** `0x1403060F8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_68(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 68

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Current MP damage: deals damage equal to the target's current MP, with no hit check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 27 bytes.
- V: Typical abilities: Manaburn.

## Calculation

```text
Damage = target's current MP (drains all MP as HP damage)
No hit check, no modifiers, always succeeds
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
