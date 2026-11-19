# Formula_72_ItemRestoreHP

- **Address:** `0x140308C30`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_72(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`); reached as slot 72 of the formula registry through Battle_ResolveAction
- **Callees:** Item_GetChemistRecord, Formula_HealSwap (tail call)
- **Dispatch ID:** 72

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

HP restore item: heals 10 x the item's amount byte (an Undead target takes it as damage). No hit roll.

## Behavior

- V: it rebuilds the item id from the chemist slot byte at `0x1407B077E` (g_FormulaBlock +0x0E): the writer stores the id's low byte plus `0x10`, and this body adds `0xF0` to complete the round trip (the `0x10` is not an operand here).
- V: only the low byte of the id survives that round trip; an item whose low byte is `0xF0` or above rebuilds as one of 240..255 instead of itself.
- V: it calls Item_GetChemistRecord for the rebuilt id, multiplies the row's byte +1 (the amount) by ten and stores it in the result's HP word (+6).
- V: it ends with a tail call to Formula_HealSwap, which turns the amount into an HP heal, or leaves it as damage when the target is Undead.
- V: no hit roll in the body.
- I: the stock users are the three HP potions; the amount byte is stored in tens (an amount of 3 heals 30).

## Calculation

```text
Amount = 10 x chemist record byte +1
then Formula_HealSwap (heal; Undead: damage)
```

## State touched

- Calls: [Formula_HealSwap](Formula_HealSwap.md)
- Reads: [g_ActionItemIdByte](../globals/g_ActionItemIdByte.md)

## Notes

- V: the whole function was read (IDA, 2026-11-18); the registry slot was confirmed against the dispatcher's index expression.
- Formula 72 is one of the twelve formula ids with a post hook row in sub_14030A11C (see FormulaHandlerContract).

## Open questions

None recorded.
