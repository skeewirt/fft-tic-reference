# Formula_CasterStatusMods

- **Address:** `0x140305D08`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_CasterStatusMods(void)`
- **Callers:** Formula_40_StealEXP, Formula_49_MonkPhysicalAveraged, Formula_50_PummelRandomHits, Formula_51_Purification, Formula_55_RushBasicPhysical, Formula_PhysMods, and 3 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The caster's status modifiers on A: Berserk raises it, Toad flattens it.

## Behavior

- V: caster +0x63 bit 0x08 (status 20, Berserk): A = A * 3 / 2.
- V: caster +0x63 bit 0x02 (status 22, Toad): A = 1.

## Referenced by

- Called by: [Formula_100_JumpDamage](Formula_100_JumpDamage.md), [Formula_99_SpeedTimesWeaponPower](Formula_99_SpeedTimesWeaponPower.md), [Formula_PhysMods](Formula_PhysMods.md), [Formula_PhysStatusHit](Formula_PhysStatusHit.md)

## Notes

56 bytes, read whole.

## Open questions

None recorded.
