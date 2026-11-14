# Formula_45_HolySword

- **Address:** `0x1403084C4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_45(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 45

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Holy Sword: PA x (WP + Y) through the physical chain, then a status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 113 bytes.
- V: Typical abilities: Judgment Blade, Cleansing Strike, Northswain's Strike, Hallowed Bolt, Divine Ruination.

## Calculation

```text
Damage = PA × (WP + Y) × [×2 dual wield] × [×3/2 Berserk/AttackUp]
 × [×2/3 target Protect] × [×3/2 target Sleep]
 × Zodiac(50-150%) × [critical] × [element absorb/weak/half]
capped at 32767, then status applied
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
