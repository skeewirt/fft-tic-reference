# Formula_ChanceSum

- **Address:** `0x140305F4C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_ChanceSum(void)`
- **Callers:** Formula_11_FaithBasedBuff, Formula_13_RaiseRevive, Formula_14_DeathInstantKill, Formula_18_Quick, Formula_20_GolemShield, Formula_26_StatSap, and 17 more (IDA code references)
- **Callees:** Formula_Zodiac

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a chance in percent in R+6: A plus the zodiac-adjusted B.

## Behavior

- V: normally B is moved into A, Formula_Zodiac runs on it, and the adjusted value is stored back as B while A returns to its old value; R+6 = A + B. Ability id 65 (g_FormulaBlock +8) skips the zodiac step and uses B as it is.
- V: the result is not capped here: Formula_ChanceRoll treats R+6 as a percent (100 and more always passes).
- V: the id-65 test is the Golem formula's (Formula_20_GolemShield); the block reads the ability word directly, so a copy of that ability under another id takes the zodiac path.

## State touched

- Calls: [Formula_Zodiac](Formula_Zodiac.md)

## Referenced by

- Called by: [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoElem](Formula_MagicHitNoElem.md), [Formula_MagicHitNoFaith](Formula_MagicHitNoFaith.md), [Formula_PhysStatusHit](Formula_PhysStatusHit.md)

## Notes

Source: block B11. 92 bytes, read whole. B is left holding the zodiac-adjusted value (WORD1 of the block is stored from the adjusted word), not restored; only A is restored. Order in the chains: it follows Formula_Zodiac and precedes Formula_FaithScale / Formula_ChanceRoll.

## Open questions

None recorded.
