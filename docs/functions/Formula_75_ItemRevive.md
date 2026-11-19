# Formula_75_ItemRevive

- **Address:** `0x140308C98`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_75(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`); reached as slot 75 of the formula registry through Battle_ResolveAction
- **Callees:** Formula_RevivePrecheck, Item_GetChemistRecord, Battle_Rand15, Formula_HealSwap
- **Dispatch ID:** 75

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Revive item: on a target being revived, heals a random 1 to the item's amount byte; on an Undead target, damage equal to its current HP.

## Behavior

- V: it calls Formula_RevivePrecheck first and returns without writing anything when that returns 0 (no status pending and the target is not Undead).
- V: when the target (g_BattleActingUnit) has bit `0x10` at +0x61 (Undead) it copies the target's current HP (+0x30) into the result's HP word (+6) and skips the item value.
- V: otherwise it rebuilds the item id from the chemist slot byte at `0x1407B077E` by adding `0xF0`, calls Item_GetChemistRecord, reads the row's byte +1 (the amount), multiplies a Battle_Rand15 value by it, shifts the product down by fifteen bits and adds one: a random 1..amount.
- V: it ends by calling Formula_HealSwap: a heal on a living target, damage on an Undead one.
- I: so the item revives with a random HP from 1 to its amount (not scaled by ten, unlike formulas 72 and 73), and destroys an Undead target outright.
- I: the stock user is the one revive item.

## Calculation

```text
Formula_RevivePrecheck must pass (a status is pending, or the target is Undead)
Undead target: amount = target current HP (damage, through Formula_HealSwap)
otherwise:     amount = 1 + random(0 .. amount byte - 1)   (chemist record byte +1)
then Formula_HealSwap
```

## State touched

- Calls: [Formula_RevivePrecheck](Formula_RevivePrecheck.md), [Battle_Rand15](Battle_Rand15.md), [Formula_HealSwap](Formula_HealSwap.md)
- Reads: [g_ActionItemIdByte](../globals/g_ActionItemIdByte.md), [g_BattleActingUnit](../globals/g_BattleActingUnit.md)

## Notes

- V: the whole function was read (IDA, 2026-11-18).
- Formula 75 is one of the twelve formula ids with a post hook row in sub_14030A11C (see FormulaHandlerContract).

## Open questions

None recorded.
