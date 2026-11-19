# Formula_29_DancerDances

- **Address:** `0x140307B44`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_29(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 29

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Dances: an X percent roll, then an effect chosen by the ability id: MP or HP damage of weapon-type value + WP, Speed, PA or MA - 1, a status, or the all-stats change downward.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation said PA + Y and stats up; the body adds the weapon-type value and WP (no Y read) and writes 1 (bit 7 clear = lower).
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 203 bytes.
- V: Typical abilities: Witch Hunt, Mincing Minuet, Slow Dance, Polka, Heathen Frolic, Forbidden Dance, Last Waltz.
- V: The earlier sheet described a generic dancer branch; the current branches are damage, stat up, all buffs and status.
- V: the effect is chosen by the ability id at 0x1407B0778: the cases are 93(a word amount at +10, flag 32), 94 (a word amount at +6, flag 0x80), 95, 96, 97 (result bytes +20, +22, +23), 98 (Formula_56 status) and 99 (byte +21); every other id only sets the result flag and has no further effect.

## Calculation

```text
Fails at once when the target has status byte +0x65 bit 0x10
Roll: Formula_BardDancerGate (X percent); then sub_140305A48 (A = weapon-type value, B = WP)
Ability 93: MP damage = A + B; 94: HP damage = A + B
95 / 96 / 97: Speed / PA / MA change byte = 1 (lower by 1)
98: Formula_56_StatusOnlyApplication; 99: all-stats byte (R+21) = 0x7F
any other id: kind bits 1 only
```

## Referenced by

- Observed behaviours: [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md), [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
