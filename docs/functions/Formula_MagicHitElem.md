# Formula_MagicHitElem

- **Address:** `0x140307028`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_MagicHitElem(void)`
- **Callers:** Formula_09_Gravity, Formula_10_FaithBasedStatus, Formula_27_Magicksap, Formula_97_MagicBasedBraveModify
- **Callees:** Formula_Zodiac, Formula_ElemBoostAction, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_ChanceSum, Formula_FaithScale, Formula_ChanceRoll

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic hit chance with the element boost and the faith factor: sets A = MA and B = X, runs the magic modifier chain, then the chance roll.

## Behavior

- V: A (g_FormulaBlock +0) = caster MA (+0x3F); B (+2) = the ability record copy's byte +9, X (block +0x2D).
- V: calls in this order: Formula_ElemBoostAction, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_Zodiac, Formula_ChanceSum, Formula_FaithScale, Formula_ChanceRoll.
- V: returns 1 when R+0 is 0 after the roll (the chance failed), else 0.
- V: four handlers call it directly (9, 10, 27 and 97); the sibling blocks drop one step: Formula_MagicHitNoElem drops the element boost, Formula_MagicHitNoFaith drops the faith factor.

## State touched

- Calls: [Formula_Zodiac](Formula_Zodiac.md), [Formula_ElemBoostAction](Formula_ElemBoostAction.md), [Formula_CasterMagMods](Formula_CasterMagMods.md), [Formula_TargetPassiveMag](Formula_TargetPassiveMag.md), [Formula_TargetStatusMag](Formula_TargetStatusMag.md), [Formula_ChanceSum](Formula_ChanceSum.md), [Formula_FaithScale](Formula_FaithScale.md), [Formula_ChanceRoll](Formula_ChanceRoll.md)

## Notes

95 bytes, read whole. Crosscheck: X (block +0x2D) is the byte at 0x1407B079D, byte 13 of the item at 0x1407B0790, a RIP-relative operand.

## Open questions

None recorded.
