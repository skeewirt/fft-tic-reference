# Formula_29_DancerDances

- **Address:** `0x140307B44`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_29(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 29

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Dancer dances: a hit roll and weapon-damage setup with per-ability branches for damage, stat ups, all buffs and status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 203 bytes.
- V: Typical abilities: Witch Hunt, Mincing Minuet, Slow Dance, Polka, Heathen Frolic, Forbidden Dance, Last Waltz.
- V: The earlier sheet described a generic dancer branch; the current branches are damage, stat up, all buffs and status.
- V: the effect is chosen by the ability id at 0x1407B0778: the cases are 93 (a word amount at +10, flag 32), 94 (a word amount at +6, flag 0x80), 95, 96, 97 (result bytes +20, +22, +23), 98 (Formula_56 status) and 99 (byte +21); every other id only sets the result flag and has no further effect.

## Calculation

```text
Hit roll: X% chance (4D5C), then weapon-damage setup
Branches by ability:
 MP damage = PA + Y
 HP damage = PA + Y
 Speed, PA or MA up (+1)
 all buffs
 otherwise status via F56
```

## Referenced by

- Observed behaviours: [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
