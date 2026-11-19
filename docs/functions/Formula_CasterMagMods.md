# Formula_CasterMagMods

- **Address:** `0x140305CB0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_CasterMagMods(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_11_FaithBasedBuff, Formula_12_MagicalHealing, Formula_13_RaiseRevive, Formula_14_DeathInstantKill, Formula_18_Quick, and 13 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The caster's magic damage modifiers: two passive bits scale A.

## Behavior

- V: caster +0x99 bit 0x04: A = A * 4 / 3.
- V: caster +0x9B bit 0x01: A = A * 3 / 2 (applied to the value left by the first step).

## Referenced by

- Called by: [Formula_04_MagicGun](Formula_04_MagicGun.md), [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoElem](Formula_MagicHitNoElem.md), [Formula_MagicHitNoFaith](Formula_MagicHitNoFaith.md)

## Notes

Block B18 (2026-11-12): 86 bytes, read whole. I: the two bits read as support abilities that raise magic power; the abilities are not named here.

## Open questions

None recorded.
