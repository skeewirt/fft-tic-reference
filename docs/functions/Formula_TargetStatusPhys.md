# Formula_TargetStatusPhys

- **Address:** `0x140305DF0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_TargetStatusPhys(void)`
- **Callers:** Formula_40_StealEXP, Formula_49_MonkPhysicalAveraged, Formula_50_PummelRandomHits, Formula_55_RushBasicPhysical, Formula_PhysMods, Formula_PhysStatusHit, and 2 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The target's status modifiers against a physical hit.

## Behavior

- V: target +0x64 bit 0x20 (status 26, Protect): A = A * 2 / 3.
- V: target +0x65 bit 0x10 (status 35, Sleep) or +0x61 bit 0x08 (status 4, Readying): A = A * 3 / 2.
- V: target +0x63 bits 0x06 (statuses 21 Chicken and 22 Toad): A = A * 3 / 2.

## Referenced by

- Called by: [Formula_100_JumpDamage](Formula_100_JumpDamage.md), [Formula_99_SpeedTimesWeaponPower](Formula_99_SpeedTimesWeaponPower.md), [Formula_PhysMods](Formula_PhysMods.md), [Formula_PhysStatusHit](Formula_PhysStatusHit.md)
- Observed behaviours: [BattleStatChangeAndCtGainSteps](../behaviors/BattleStatChangeAndCtGainSteps.md)

## Notes

114 bytes, read whole. The statuses are numbered so that status s is bit 0x80 >> (s & 7) of byte +0x61 + (s >> 3). A leaf function (no unwind entry) with 8 call sites.

## Open questions

None recorded.
