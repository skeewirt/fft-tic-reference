# Formula_PhysStatusHit

- **Address:** `0x1403070E4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_PhysStatusHit(void)`
- **Callers:** Formula_38_StealEquipment, Formula_39_StealGil, Formula_77_PhysicalHPDrain, Formula_79_PhysicalMissingHP, Formula_80_PhysicalStatus
- **Callees:** Formula_Zodiac, sub_140305C18, Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys, Formula_ChanceSum, Formula_ChanceRoll

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Physical status chance: runs the physical caster and target modifier chain on A, adds the zodiac step and rolls the chance. The caller sets A and B first.

## Behavior

- V: it does not set A or B itself: the calling handler stores both (A = the stat, B = X) before the call.
- V: calls sub_140305C18 (caster physical modifiers), Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys, Formula_Zodiac, Formula_ChanceSum, Formula_ChanceRoll in that order (no faith factor, no element boost).
- V: returns 1 when R+0 is 0 after the roll, else 0.
- V: IDA labelled this address __acrt_eagerly_load_locale_apis_0 (a library-name mislabel).

## State touched

- Calls: [Formula_Zodiac](Formula_Zodiac.md), [sub_140305C18](sub_140305C18.md), [Formula_CasterStatusMods](Formula_CasterStatusMods.md), [Formula_TargetPassivePhys](Formula_TargetPassivePhys.md), [Formula_TargetStatusPhys](Formula_TargetStatusPhys.md), [Formula_ChanceSum](Formula_ChanceSum.md), [Formula_ChanceRoll](Formula_ChanceRoll.md)

## Notes

58 bytes, read whole (2026-11-12).

## Open questions

None recorded.
