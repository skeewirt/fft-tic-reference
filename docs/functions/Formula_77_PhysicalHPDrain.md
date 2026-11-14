# Formula_77_PhysicalHPDrain

- **Address:** `0x140308D48`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_77(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 77

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Physical HP drain: a magic-style hit check then percentage-of-max-HP damage that heals the caster.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 113 bytes.
- V: Typical abilities: Bloodfeast, Drain Touch.
- V: The earlier sheet said the caster recovers MP; the current code recovers HP.

## Calculation

```text
Physical evade check, then MA + X through the magic chain
Damage = (Y × target MaxHP + 99) / 100
Caster recovers HP equal to the damage dealt
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
