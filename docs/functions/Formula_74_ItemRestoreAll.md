# Formula_74_ItemRestoreAll

- **Address:** `0x140308C70`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_74(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** Formula_HealSwap
- **Dispatch ID:** 74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Full restore item: HP healed = the target's max HP and MP healed = its max MP (an Undead target takes the max HP as damage).

## Behavior

- V: it writes the target's max HP (unit +0x32) to the result's HP word (+6) and its max MP (+0x36) to the MP heal word (+0x0C), kind byte (+0x27) = 0x90, then tail-calls Formula_HealSwap.
- V: no hit roll and no item value read: the amount is the target's own maximum.
- I: Formula_HealSwap sets the kind byte to 0x80 on an Undead target, so the MP heal bit is dropped there.
- I: the stock user is one chemist item.

## Calculation

```text
R+6 = target max HP (+0x32), R+12 = target max MP (+0x36), kind bits 0x90
then Formula_HealSwap (HP becomes a heal; Undead: damage)
```

## State touched

- Calls: [Formula_HealSwap](Formula_HealSwap.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
