# Formula_81_MonsterBuffHealMagicHitStatus

- **Address:** `0x140308E90`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_81(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 81

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Status with a magic chance: MA + X with the element boost, the caster's magic modifiers and zodiac (no Faith); on success the ability's status through Formula_56.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation listed a Faith factor; the body calls no faith step.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 83 bytes.
- V: Typical abilities: Choco Esuna, Guardian Nymph, Shell Nymph.

## Calculation

```text
Chance: A = MA, B = X; Formula_ElemBoostAction, Formula_CasterMagMods, Formula_Zodiac,
  Formula_ChanceSum, Formula_ChanceRoll (no Faith)
On success: Formula_56_StatusOnlyApplication
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
