# Formula_47_DuskbladeMPDrain

- **Address:** `0x140308664`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_47(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 47

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Duskblade: PA x WP physical damage that restores the caster's MP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 70 bytes.
- V: Typical abilities: Duskblade.
- V: The earlier sheet's parenthetical was inverted; Duskblade drains MP.

## Calculation

```text
Physical evade check
Damage = PA × WP through the physical chain
 (dual wield, Berserk/AttackUp, Protect, Sleep, Zodiac, critical)
Caster recovers MP equal to the damage dealt
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
