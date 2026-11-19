# Skillset_GetAbility

- **Address:** `0x140275860`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `uint16_t Skillset_GetAbility(int setId, int slot)`
- **Callers:** Skillset_BuildAbilityList, sub_14020D190, sub_14021DE98, sub_140271EFC, sub_14027612C, sub_1402781A8, sub_140278358, sub_14030CD08, sub_14030DD8C, sub_14030E368, sub_14030EC48
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the ability id stored in one slot of a skillset, or 0 when the set or slot does not exist.

## Behavior

- V: three storage blocks. Sets 0..175: 25 bytes each at 0x14067E210, slots 0..21. Sets 224..226: the same 25-byte layout directly after set 175 (at 0x14067F340). Sets 176..223: 5 bytes each at 0x14067F4C0, slots 0..3.
- V: 25-byte set: 3 flag bytes, then 22 low bytes. 5-byte set: 1 flag byte, then 4 low bytes.
- V: the id is the low byte plus 0x100 when the slot's flag bit is set; the flag for slot k is bit 7 - (k mod 8) of flag byte k / 8, so ids reach 0x1FF.
- V: any other set id (227 and above), or a slot beyond the block's range, returns 0.
- I: slots 0..15 are the action abilities and 16..21 the reaction, support and movement slots; one caller walks 16..21 separately.
- V: a negative set id falls into the first block and a negative slot reads before the row (no lower-bound check).
- V: leaf; writes rax, rcx, rdx, r8, r9, r10 only.
- V (2026-10-29 census): the only code that reads the three blocks. Three other operands land inside them by displacement but read other tables: UnitWork_InitFromSpawnRecord (the JobNeedLevel rows through the virtual base 0x14067F384) and sub_140281A64 / sub_140282E38 (a byte table at the virtual base 0x14067F58A indexed by an action id; whether an index below 0x26 can occur is open).

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Job_ReadLearnedBitsForBattle](Job_ReadLearnedBitsForBattle.md), [SaveWork_UnpackToLive_Repair](SaveWork_UnpackToLive_Repair.md), [Skillset_BuildAbilityList](Skillset_BuildAbilityList.md), [Unit_ApplySpawnRecord](Unit_ApplySpawnRecord.md), [Unit_BuildRsmAbilityList](Unit_BuildRsmAbilityList.md), [Unit_QueueJobAbilitiesToLearn](Unit_QueueJobAbilitiesToLearn.md), [sub_140271EFC](sub_140271EFC.md), [sub_14030CD08](sub_14030CD08.md), [sub_14030DD8C](sub_14030DD8C.md), [sub_14030E368](sub_14030E368.md), [sub_14030EC48](sub_14030EC48.md)
- Observed behaviours: [SkillsetIdsPastTheByte](../behaviors/SkillsetIdsPastTheByte.md)
- Reads tables: [SkillsetTable](../tables/SkillsetTable.md), [SkillsetTableMonster](../tables/SkillsetTableMonster.md), [SkillsetTableSpecial](../tables/SkillsetTableSpecial.md)

## Notes

The set id of a job is byte 0 of its JobTable row. Sets 224..226 belong to special characters; 176..223 are monster sets.
Proposed data names: g_SkillsetTable (176 x 25), g_SkillsetTableMonster (48 x 5), g_SkillsetTableSpecial (3 x 25) (the IDB already uses these).

- Correction: a leaf function with three `img` table references.

## Open questions

None recorded.
