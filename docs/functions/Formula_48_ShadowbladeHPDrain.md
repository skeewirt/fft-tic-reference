# Formula_48_ShadowbladeHPDrain

- **Address:** `0x1403086AC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_48(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shadowblade: PA x WP physical damage that heals the caster for the damage dealt.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 70 bytes.
- V: Typical abilities: Shadowblade.
- V: The earlier sheet's parenthetical was inverted; Shadowblade drains HP.

## Calculation

```text
Physical evade check
Damage = PA × WP through the physical chain
 (dual wield, Berserk/AttackUp, Protect, Sleep, Zodiac, critical)
Caster recovers HP equal to the damage dealt
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
