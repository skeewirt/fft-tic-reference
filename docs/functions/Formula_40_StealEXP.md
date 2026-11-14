# Formula_40_StealEXP

- **Address:** `0x1403080F8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_40(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 40

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steal EXP: a physical evade check and a Speed-based hit, then a CT/EXP modifier.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 270 bytes.
- V: Typical abilities: Steal EXP.
- V: The earlier sheet described an EXP/level transfer; the current code writes a CT/EXP modifier capped by target CT.

## Calculation

```text
Physical evade check, then Speed + X through the magic chain
CT/EXP modifier = min(Y + caster Speed, 100), capped by target CT
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
