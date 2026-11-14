# Formula_79_PhysicalMissingHP

- **Address:** `0x140308DF4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_79(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 79

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Physical plus missing HP: a physical evade check and magic chain, then damage equal to the caster's missing HP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 89 bytes.
- V: Typical abilities: Goblin Punch.
- V: The earlier sheet used the target's missing HP; the current code uses the caster's.

## Calculation

```text
Physical evade check, then magic chain
Damage = caster MaxHP - caster current HP
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
