# Formula_37_RendEquipment

- **Address:** `0x140307E74`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_37(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 37

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Break equipment: when Action_PickTargetEquipment finds a piece it resolves a sub-action; otherwise the physical evade gate, then a chance of PA + WP + Y; on success (and past Formula_StealGate) the flag word gets the break bit 0x04.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation called it PA x WP damage; the body rolls a chance and writes no damage.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 342 bytes.
- V: Typical abilities: Rend Helm/Armor/Shield/Weapon.
- V: The earlier sheet described a simple dual strike; the current code recursively dispatches a sub-action.

## Calculation

```text
Action_PickTargetEquipment != 0: Battle_ResolveAction of a sub-action (caster +0x1A0), flag 0x2000 on a miss
else Gate: sub_140306C90 (physical evade)
Chance: A = PA, B = WP + Y; Formula_PhysMods, Formula_ChanceSum, Formula_ChanceRoll
Failure: flag word (+18) = 0x2000 outside a forecast
Success: Formula_StealGate; still a hit -> flag word = 4
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

The recursive sub-action's exact semantics and the second-hit condition.
