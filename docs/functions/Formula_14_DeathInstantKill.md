# Formula_14_DeathInstantKill

- **Address:** `0x140307640`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_14(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 14

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Instant death: a magic hit check followed by percentage-of-max-HP damage, with undead and immunity handling.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 262 bytes.
- V: Typical abilities: Death.

## Calculation

```text
Hit = (MA_modified + X_with_zodiac)
 where MA = MA × [×5/4 element] × [×4/3 MagicAttackUp]
 + [×2/3 Shell] × [×3/2 Sleep] (if not Undead bypass)
 × Zodiac × Faith(caster×target/10000)
On hit: Damage = (Y × MaxHP + 99) / 100
Undead → heals instead | Immune → miss | Reflect → bounced
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
