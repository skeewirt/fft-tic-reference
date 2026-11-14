# Formula_TargetPassiveMag

- **Address:** `0x140305D98`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_TargetPassiveMag(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_14_DeathInstantKill, Formula_26_StatSap, Formula_31_IaidoNether, Formula_33_DrawOutDamageStatus, Formula_MagicDamageTail, and 4 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The target's passive modifiers against a magic hit.

## Behavior

- V: target +0x99 bit 0x02: A = A * 2 / 3.
- V: target +0x9B bit 0x01: A = A * 3 / 2 (on the value left by the first step).

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoElem](Formula_MagicHitNoElem.md), [Formula_MagicHitNoFaith](Formula_MagicHitNoFaith.md)

## Notes

Source: block B21. 85 bytes, read whole.

## Open questions

None recorded.
