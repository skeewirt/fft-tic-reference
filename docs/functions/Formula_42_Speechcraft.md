# Formula_42_Speechcraft

- **Address:** `0x140308284`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_42(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 42

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Speechcraft: a magic hit check with per-ability branches for buffs, Brave/Faith changes, a level/speed transfer and status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 366 bytes.
- V: Typical abilities: Entice, Stall, Praise, Intimidate, Preach, Enlighten, Condemn, Insult, Mimic Darlavon.
- V: The earlier sheet named ability 123 Nether Mantra; the current code routes it through the level/speed transfer helper.
- V: the branches are chosen by the ability id at 0x1407B0778: the compares are for the ids 117, 118, 119, 120, 121 and 123; any other id (122 included) takes none of these branches.

## Calculation

```text
Hit = (MA + X) × Zodiac(50-150%) × Faith(caster×target/10000)
Branches by ability:
 all buffs; Brave up/down; Faith up/down; level/speed transfer; otherwise F56 status
```

## Referenced by

- Observed behaviours: [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

What ability 123 does; its helper is shared with Steal Gil.
