# Formula_84_MPRestorationMagicBased

- **Address:** `0x140308FA0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_84(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 84

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MP restoration: MA x Y MP healing with caster boost and Zodiac; always succeeds.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 85 bytes.
- V: Typical abilities: Magick Nymph.

## Calculation

```text
Heal MP = MA × Y × [×4/3 MagicAttackUp] × Zodiac(50-150%)
(No hit check — always succeeds. Heals MP, not HP)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
