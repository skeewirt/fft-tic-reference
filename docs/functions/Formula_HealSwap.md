# Formula_HealSwap

- **Address:** `0x140306378`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_HealSwap(void)`
- **Callers:** Formula_12_MagicalHealing, Formula_13_RaiseRevive, Formula_35_DrawOutHeal, Formula_53_Revive, Formula_76_MagicHealSimplified, Formula_87_BequeathBaconSelfSacrifice, and 4 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns the computed amount into a heal, or into damage when the target is Undead.

## Behavior

- V: target +0x61 bit 0x10 (status 3, Undead): R+39 = 0x80 (the amount stays damage in R+6) and the low byte of dword 0x14186B028 is cleared.
- V: otherwise R+8 = R+6, R+6 = 0 and R+39 = (R+39 & 0x3F) | 0x40.

## State touched

- Writes: [ActionResult.hp_heal](../structs/ActionResult.md#hp_heal), [ActionResult.kind_bits](../structs/ActionResult.md#kind_bits)

## Referenced by

- Called by: [Formula_07_WeaponHeal](Formula_07_WeaponHeal.md), [Formula_72_ItemRestoreHP](Formula_72_ItemRestoreHP.md), [Formula_74_ItemRestoreAll](Formula_74_ItemRestoreAll.md), [Formula_75_ItemRevive](Formula_75_ItemRevive.md)

## Notes

Source: block B32. 63 bytes, read whole. Called by ten handlers (the heal and revive formulas). Crosscheck: 0x3F and 0x40 sit in the second path of the function (after the first return), where the checker leaf scan stops.

## Open questions

? what the dword 0x14186B028 low byte carries (it is also read by sub_14030A11C).
