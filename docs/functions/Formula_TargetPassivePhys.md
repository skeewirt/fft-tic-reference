# Formula_TargetPassivePhys

- **Address:** `0x140305D40`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_TargetPassivePhys(void)`
- **Callers:** Formula_40_StealEXP, Formula_49_MonkPhysicalAveraged, Formula_50_PummelRandomHits, Formula_55_RushBasicPhysical, Formula_PhysMods, Formula_PhysStatusHit, and 2 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The target's passive modifiers against a physical hit.

## Behavior

- V: target +0x99 bit 0x08: A = A * 2 / 3.
- V: target +0x9B bit 0x01: A = A * 3 / 2 (on the value left by the first step).

## Referenced by

- Called by: [Formula_PhysMods](Formula_PhysMods.md), [Formula_PhysStatusHit](Formula_PhysStatusHit.md)

## Notes

Block B20 (2026-11-12): 85 bytes, read whole.

## Open questions

None recorded.
