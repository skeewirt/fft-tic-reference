# Formula_MagicHitNoElem

- **Address:** `0x140306FCC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_MagicHitNoElem(void)`
- **Callers:** Formula_15_MPDrainMagical, Formula_16_HPDrainMagical, Formula_21_Return, Formula_22_Disempower, Formula_23_Gravija
- **Callees:** Formula_Zodiac, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_ChanceSum, Formula_FaithScale, Formula_ChanceRoll

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic hit chance without the element boost: A = MA, B = X, then the magic modifier chain, the faith factor and the chance roll.

## Behavior

- V: A = caster MA (+0x3F); B = X (the ability record copy's byte +9, block +0x2D).
- V: calls Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_Zodiac, Formula_ChanceSum, Formula_FaithScale, Formula_ChanceRoll in that order.
- V: returns 1 when R+0 is 0 after the roll, else 0.

## State touched

- Calls: [Formula_Zodiac](Formula_Zodiac.md), [Formula_CasterMagMods](Formula_CasterMagMods.md), [Formula_TargetPassiveMag](Formula_TargetPassiveMag.md), [Formula_TargetStatusMag](Formula_TargetStatusMag.md), [Formula_ChanceSum](Formula_ChanceSum.md), [Formula_FaithScale](Formula_FaithScale.md), [Formula_ChanceRoll](Formula_ChanceRoll.md)

## Notes

Formula block B05 (2026-11-12): 90 bytes, read whole. Siblings: Formula_MagicHitElem (adds the element boost), Formula_MagicHitNoFaith (drops the faith factor). Crosscheck: X (block +0x2D) is the byte at 0x1407B079D, byte 13 of the item at 0x1407B0790, a RIP-relative operand.

## Open questions

None recorded.
