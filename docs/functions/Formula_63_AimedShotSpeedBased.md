# Formula_63_AimedShotSpeedBased

- **Address:** `0x140308A70`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_63(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 63

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Aimed Shot: a Speed-based hit check that inflicts a status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 73 bytes.
- V: Typical abilities: Leg Shot, Arm Shot.

## Calculation

```text
Hit = (Speed + X) × [×2 dual wield] × [×3/2 Berserk/AttackUp]
 × [×2/3 target Protect] × [×3/2 Sleep] × Zodiac
 × faith_scaling
On success: inflicts status (ADDITIVE, uses SPEED not PA!)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
