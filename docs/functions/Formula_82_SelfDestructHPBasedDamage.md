# Formula_82_SelfDestructHPBasedDamage

- **Address:** `0x140308EE4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_82(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 82

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Self-destruct: HP-based damage, with a different value for self versus area targets.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 67 bytes.
- V: Typical abilities: Self-Destruct.

## Calculation

```text
If caster == source (self-target): Damage = CurHP
If caster ≠ source (AoE target):  Damage = MaxHP - CurHP
Then: status applied via F56
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
