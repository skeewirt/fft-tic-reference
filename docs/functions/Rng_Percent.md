# Rng_Percent

- **Address:** `0x140278E68`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `bool Rng_Percent(int scale, int threshold)`
- **Callers:** 22 functions, among them Formula_56_StatusOnlyApplication, Formula_42_Speechcraft, Formula_55_RushBasicPhysical, Formula_ChanceRoll, Formula_EvadeByteRoll, Formula_StatusChance19, BattleAction_BuildReaction, Unit_RollAbilityLearning, Unit_TryLearnAbility
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a battle random number and tells whether it reaches a threshold on a given scale.

## Behavior

- V: steps the xorshift state at 0x1408E5FC8 (four dwords) exactly as Battle_Rand15 does and takes the low 15 bits of the newest dword as r.
- V: returns whether scale * r / 0x8000 is at least threshold (signed integer arithmetic; the division is compiled as a shift by 15, so 0x8000 is not an operand).
- V: unlike Battle_Rand15 it has no forecast branch: it draws even while g_BattleSimulating is set.
- V: Formula_56_StatusOnlyApplication calls it as Rng_Percent(100, 24) once per listed status in its per-status chance mode (the flag 0x20 of the inflict copy, tested in Formula 56, not here): a true result takes that status out of the list.

## Referenced by

- Called by: [Formula_BardDancerGate](Formula_BardDancerGate.md), [Formula_ChanceRoll](Formula_ChanceRoll.md), [Formula_DrawOutGate](Formula_DrawOutGate.md), [Formula_EvadeByteRoll](Formula_EvadeByteRoll.md), [Formula_StatusChance19](Formula_StatusChance19.md), [Unit_TryLearnAbility](Unit_TryLearnAbility.md), [sub_140271EFC](sub_140271EFC.md), [sub_14030BE18](sub_14030BE18.md), [sub_14030BE68](sub_14030BE68.md), [sub_14030CD08](sub_14030CD08.md)

## Notes

Name is ours. 115 bytes, read whole (2026-11-12). It shares its state with Battle_Rand15 (the open question of that sheet): both read and advance 0x1408E5FC8.

## Open questions

None recorded.
