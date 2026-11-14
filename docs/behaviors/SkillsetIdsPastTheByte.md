# SkillsetIdsPastTheByte

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Ability data](../areas/ability-data.md)
- **Affects:** [Skillset_GetAbility](../functions/Skillset_GetAbility.md), [Skillset_BuildAbilityList](../functions/Skillset_BuildAbilityList.md), [JobCommandTable_GetRow](../functions/JobCommandTable_GetRow.md), [UnitWork_ApplyJobRow](../functions/UnitWork_ApplyJobRow.md), [Battle_ResolveAction](../functions/Battle_ResolveAction.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A skillset id is one byte everywhere the game keeps it (job row +0, unit +0x12 / +0x13 / +0x192, save A+7, the action's command byte +0x1A1, the battle menu arrays, the command table).

## Behavior

- V (code): 242 sites; the 8-bit tests (17 monster range tests, the job rule 5..0x17, 0xE0, 0x18, 0x14, 7 / 8, the 0xFF terminators); the uses as an identity are the set arguments of Skillset_GetAbility / BuildAbilityList / BuildTabAbilityList / FindJobBySkillset, the g_CommandKind index, the name and help tokens 0xB000 / 0x9800 + set, equality tests of two sets, and stores of a whole id into a byte.

## Open questions

None recorded.
