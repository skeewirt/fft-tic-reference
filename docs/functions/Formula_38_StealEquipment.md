# Formula_38_StealEquipment

- **Address:** `0x140307FCC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_38(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 38

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Steal equipment: an equipment-slot check then a Speed-based hit; success steals the item.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 204 bytes.
- V: Typical abilities: Steal Helm/Armor/Shield/Weapon/Accessory.
- V: The earlier sheet described a Speed difference; the current code uses Speed + X.

## Calculation

```text
Equipment-slot check; no slot -> miss
Physical evade check, then Speed + X through the magic chain
On success: steals the item (attack-type flags = 16)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
