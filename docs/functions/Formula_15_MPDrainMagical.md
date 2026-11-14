# Formula_15_MPDrainMagical

- **Address:** `0x140307748`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_15(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 15

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MP drain: a magic hit check then MP damage based on the target's maximum MP, restoring the caster's MP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 85 bytes.
- V: Typical abilities: Empowerment, Syphon.
- V: The earlier sheet labelled this HP drain; the current code drains MP.

## Calculation

```text
Damage = (Y × target MaxMP + 99) / 100
Caster recovers MP equal to the damage dealt
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
