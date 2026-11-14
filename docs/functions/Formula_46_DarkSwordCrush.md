# Formula_46_DarkSwordCrush

- **Address:** `0x140308538`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_46(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 46

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Dark Sword (Crush): PA x WP physical damage that also destroys a piece of equipment.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 299 bytes.
- V: Typical abilities: Crush Armor, Crush Helm, Crush Weapon, Crush Accessory.

## Calculation

```text
Damage = PA × WP × [phys modifiers] × Zodiac × [critical]
 × [element absorb/weak/half]
Dual wield: PA halved for off-hand hit
On success: destroys target equipment + deals damage
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
