# Formula_28_BardSongs

- **Address:** `0x140307A70`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_28(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 28

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Songs: an X percent roll (Formula_BardDancerGate), then an effect chosen by the ability id: MP or HP restore of MA + Y, Speed, PA or MA + 1, a status, or every stat up.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation said the stats go down; the bytes written are 0x81 (bit 7 = raise).
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 212 bytes.
- V: Typical abilities: Seraph Song, Life's Anthem, Rousing Melody, Battle Chant, Magickal Refrain, Nameless Song, Finale.
- V: The earlier sheet used ability IDs 117-123; the current branch IDs are 86-92 and the branches differ.
- V: the effect is chosen by the ability id at 0x1407B0778: the cases are 86(a word amount at +12 and flag 16), 87 (a word amount at +8 and flag 64), 88, 89, 90 (result bytes +20, +22, +23), 91 (Formula_56 status) and 92 (byte +21); every other id takes the default branch, which only sets the result flag, so the same row under any other ability number has no effect.

## Calculation

```text
Fails at once when the target has status byte +0x65 bit 0x10
Roll: Formula_BardDancerGate (X percent)
Ability 86: MP heal = MA + Y; 87: HP heal = MA + Y
88 / 89 / 90: Speed / PA / MA change byte = 0x81 (raise by 1)
91: Formula_56_StatusOnlyApplication; 92: all-stats byte (R+21) = 0xFF
any other id: kind bits 1 only
```

## Referenced by

- Observed behaviours: [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
