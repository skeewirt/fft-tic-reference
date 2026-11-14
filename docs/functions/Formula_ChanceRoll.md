# Formula_ChanceRoll

- **Address:** `0x140306408`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_ChanceRoll(void)`
- **Callers:** Formula_11_FaithBasedBuff, Formula_13_RaiseRevive, Formula_14_DeathInstantKill, Formula_18_Quick, Formula_20_GolemShield, Formula_26_StatSap, and 16 more (IDA code references)
- **Callees:** Rng_Percent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns R+6 (a chance in percent) into the shown hit percent and the roll that can make the action miss.

## Behavior

- V: chance = R+6, then R+6 is cleared. Below 100 only: R+44 = chance * R+44 / 100.
- V: the roll runs when g_BattleSimulating is 0 or the chance is 0: Rng_Percent(100, chance) true (failed) stores R+0 = 0, R+2 = 6, R+6 = 0.
- V: a chance of 100 or more changes nothing (always passes).

## State touched

- Calls: [Rng_Percent](Rng_Percent.md)
- Writes: [ActionResult.hit](../structs/ActionResult.md#hit), [ActionResult.miss_reason](../structs/ActionResult.md#miss_reason), [ActionResult.hit_percent](../structs/ActionResult.md#hit_percent)

## Referenced by

- Called by: [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoElem](Formula_MagicHitNoElem.md), [Formula_MagicHitNoFaith](Formula_MagicHitNoFaith.md), [Formula_PhysStatusHit](Formula_PhysStatusHit.md)
- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)

## Notes

Formula block B13 (2026-11-12): 115 bytes, read whole.

## Open questions

None recorded.
