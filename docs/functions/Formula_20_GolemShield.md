# Formula_20_GolemShield

- **Address:** `0x14030784C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_20(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Golem shield: a magic hit check that creates a damage-absorbing barrier.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 175 bytes.
- V: Typical abilities: Golem.

## Calculation

```text
Power = (MA + X) × [×4/3 MagicAttackUp]
 then Faith scaling (based on caster status)
On success: creates barrier, sets attack-type flags = 1
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
