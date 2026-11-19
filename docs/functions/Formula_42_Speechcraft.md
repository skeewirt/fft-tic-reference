# Formula_42_Speechcraft

- **Address:** `0x140308284`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_42(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 42

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Talk: a target with the refusing reaction may refuse on a Brave roll; then a chance of MA + X (zodiac only, no Faith) and an effect chosen by the ability id.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation listed a Faith factor; the body calls no faith step.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 366 bytes.
- V: Typical abilities: Entice, Stall, Praise, Intimidate, Preach, Enlighten, Condemn, Insult, Mimic Darlavon.
- V: The earlier sheet named ability 123 Nether Mantra; the current code routes it through the level/speed transfer helper.
- V: the branches are chosen by the ability id at 0x1407B0778: the compares are for the ids 117, 118, 119, 120, 121 and 123; any other id (122 included) takes none of these branches, so the same row under any other ability number gets none of the id-specific effects.

## Calculation

```text
No effect on a target with status byte +0x65 bit 0x10, or on a target with +6 bit 0x20 unless the caster has +0x9A bit 0x10
Refusal: target +0x97 bit 0x20: chance = target Brave -> hit 0, reaction 448, reason 11
Chance: A = MA, B = X; Formula_Zodiac, Formula_ChanceSum, Formula_ChanceRoll (no Faith)
On success: per ability id (buffs, Brave / Faith changes, transfers) or Formula_56
```

## Referenced by

- Observed behaviours: [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

What ability 123 does; its helper is shared with Steal Gil.
