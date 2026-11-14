# Formula_53_Revive

- **Address:** `0x1403088D4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_53(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 53

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Revive: a PA-based hit check then percentage-of-max-HP healing, with the undead check.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 136 bytes.
- V: Typical abilities: Revive, Squeal.

## Calculation

```text
Hit = (PA + X) × [×3/2 Berserk] × Zodiac(50-150%)
 × faith_scaling
If target dead: Heal = (Y × MaxHP + 99) / 100
then Undead reverse check
(ADDITIVE hit, but heal is HP%-based)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
