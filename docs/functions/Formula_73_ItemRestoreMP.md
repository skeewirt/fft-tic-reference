# Formula_73_ItemRestoreMP

- **Address:** `0x140306BD0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_73(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`); reached as slot 73 of the formula registry through Battle_ResolveAction
- **Callees:** Item_GetChemistRecord
- **Dispatch ID:** 73

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MP restore item: restores 10 x the item's amount byte as MP. No hit roll, no Undead rule.

## Behavior

- V: it rebuilds the item id from the chemist slot byte at `0x1407B077E` (g_FormulaBlock +0x0E) by adding `0xF0` (the writer stored the id's low byte plus `0x10`).
- V: only the low byte of the id survives that round trip: an item whose low byte is `0xF0` or above rebuilds as one of 240..255 instead of itself.
- V: it calls Item_GetChemistRecord with the rebuilt id and reads the row's byte +1, the amount.
- V: it multiplies that byte by ten (five times the byte, then doubled) and stores the product in the result's MP heal word (+0x0C).
- V: it writes `0x10` (MP heal) into the result's kind byte (+0x27).
- V: unlike formula 72 it does not call Formula_HealSwap, so an Undead target is restored like any other.
- I: the stock users are the two MP potions; the amount byte is stored in tens (an amount of 2 restores 20).

## Calculation

```text
MP heal = 10 x chemist record byte +1
kind bits = 0x10 (MP heal)
```

## State touched

- Reads: [g_ActionItemIdByte](../globals/g_ActionItemIdByte.md)

## Notes

- V: the whole function was read (IDA, 2026-11-18); the registry slot was confirmed against the dispatcher's index expression.

## Open questions

None recorded.
