# Battle_Rand15

- **Address:** `0x14030D088`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `uint16_t Battle_Rand15(void)`
- **Callers:** Formula_50_PummelRandomHits, Formula_55_RushBasicPhysical, Formula_56_StatusOnlyApplication, Formula_CritRoll, sub_140305A48, sub_1403071DC, sub_140308C98
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle's random number: a 15-bit value, fixed while a forecast runs.

## Behavior

- V: returns 0x4000 while g_BattleSimulating is non-zero (the preview draws the middle of the range).
- V: otherwise it steps a xorshift state at 0x1408E5FC8 (four dwords) and returns the low 15 bits of the newest dword.
- V: callers include Formula_CritRoll, Formula_50_PummelRandomHits, Formula_55_RushBasicPhysical, Formula_56_StatusOnlyApplication, sub_140305A48 and sub_1403071DC.

## Referenced by

- Called by: [Formula_04_MagicGun](Formula_04_MagicGun.md), [Formula_75_ItemRevive](Formula_75_ItemRevive.md), [Formula_CritRoll](Formula_CritRoll.md)

## Notes

sub_14030D088 (2026-11-12): 92 bytes, read whole. Rng_Percent(a, b) (0x140278E68) is a separate helper; this one is the formula blocks' own draw. Crosscheck: the state address 0x1408E5FC8 is used after the first return of the function (the preview branch), where the checker's leaf scan stops.

## Open questions

? whether the state at 0x1408E5FC8 is the same generator Rng_Percent uses.
