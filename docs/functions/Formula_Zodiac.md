# Formula_Zodiac

- **Address:** `0x140305178`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_Zodiac(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_11_FaithBasedBuff, Formula_12_MagicalHealing, Formula_13_RaiseRevive, Formula_14_DeathInstantKill, Formula_18_Quick, and 28 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The zodiac compatibility step on A: raises or lowers it by the pair of signs.

## Behavior

- V: signs are the top nibble of the u16 at +8 of the caster and the target; when either is 12 nothing happens.
- V: the class is byte table 0x140682F20 indexed by |caster sign - target sign| (0, 0, 0, 1, 2, 0, 3, 0, 2, 1, 0, 0 for 0..11); class 3 (opposite signs) becomes 5 unless the caster or the target has bit 0x20 of +6 set, in which case it becomes 1.
- V: percents by class from dword table 0x140723720 plus two constants: 0 = 100, 1 = 75, 2 = 125, 3 = 100, 4 = 50, 5 = 150 (a class of 6 or more = 100).
- V: A = A * (percent - 100) / 100 + A, raised to 1 when it falls below 1.
- I: class 4 (50 percent) is not reachable from the table; only 75, 100, 125 and 150 have been seen in play.

## Referenced by

- Called by: [Formula_04_MagicGun](Formula_04_MagicGun.md), [Formula_07_WeaponHeal](Formula_07_WeaponHeal.md), [Formula_100_JumpDamage](Formula_100_JumpDamage.md), [Formula_99_SpeedTimesWeaponPower](Formula_99_SpeedTimesWeaponPower.md), [Formula_ChanceSum](Formula_ChanceSum.md), [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoElem](Formula_MagicHitNoElem.md), [Formula_MagicHitNoFaith](Formula_MagicHitNoFaith.md), [Formula_PhysStatusHit](Formula_PhysStatusHit.md)

## Notes

Source: block B25. 233 bytes, read whole. A data formula that wants the stock compatibility calls this block on A; Formula_ChanceSum calls it on B.

## Open questions

? what bit 0x20 of unit +6 stands for in the opposite-signs rule (I, no equipment).
