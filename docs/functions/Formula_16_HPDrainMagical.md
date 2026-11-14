# Formula_16_HPDrainMagical

- **Address:** `0x1403077A0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_16(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 16

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

HP drain: a magic hit check then HP damage based on the target's maximum HP, restoring the caster's HP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 81 bytes.
- V: Typical abilities: Invigoration, Drain.
- V: The earlier sheet labelled this MP drain; the current code drains HP.

## Calculation

```text
Damage = (Y × target MaxHP + 99) / 100
Caster recovers HP equal to the damage dealt
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
