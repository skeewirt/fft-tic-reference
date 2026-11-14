# Formula_37_RendEquipment

- **Address:** `0x140307E74`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_37(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 37

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rend equipment: an equipment-slot check then physical damage; a recursive sub-action handles the second hit.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 342 bytes.
- V: Typical abilities: Rend Helm/Armor/Shield/Weapon.
- V: The earlier sheet described a simple dual strike; the current code recursively dispatches a sub-action.

## Calculation

```text
Equipment-slot check; if a slot is selected, a recursive sub-action is dispatched
Physical evade check, then PA × weapon power through the physical chain
On success: destroys the target's equipment in that slot
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

The recursive sub-action's exact semantics and the second-hit condition.
