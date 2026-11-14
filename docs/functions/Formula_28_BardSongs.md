# Formula_28_BardSongs

- **Address:** `0x140307A70`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_28(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 28

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Bard songs: a hit roll with per-ability branches for healing, stat downs, all buffs and status.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 212 bytes.
- V: Typical abilities: Seraph Song, Life's Anthem, Rousing Melody, Battle Chant, Magickal Refrain, Nameless Song, Finale.
- V: The earlier sheet used ability IDs 117-123; the current branch IDs are 86-92 and the branches differ.
- V: the effect is chosen by the ability id at 0x1407B0778: the cases are 86 (a word amount at +12 and flag 16), 87 (a word amount at +8 and flag 64), 88, 89, 90 (result bytes +20, +22, +23), 91 (Formula_56 status) and 92 (byte +21); every other id takes the default branch, which only sets the result flag.

## Calculation

```text
Hit roll: X% chance (4D5C)
Branches by ability:
 HP heal or MP heal = caster MA + Y
 Speed, PA or MA down (set to minimum)
 all buffs
 otherwise status via F56
```

## Referenced by

- Observed behaviours: [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
