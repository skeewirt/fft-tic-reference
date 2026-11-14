# UnitWork_FindJobBySkillset

- **Address:** `0x14028AC50`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int UnitWork_FindJobBySkillset(UnitWork *c, int skillset)`
- **Callers:** sub_14022F868 (2), sub_1402E600C (2), sub_140335140
- **Callees:** sub_14028668C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The first job of a work record's job list whose JobTable row holds `skillset`; the record's own job (+3) when none does.

## Behavior

- V: the list is sub_14028668C(c, list) (JobList_Build from the record's unlock bits at +159, mode 1).
- V: row guard per entry: job < 0xAE (stock); returns the matching job id or c +3.
- V: its fallback is the unit's job byte +3 (at 0x14028ACB5); 0x14028ACB9 is a branch target; the loop before it walks the unit's job list.

## State touched

- Calls: [sub_14028668C](sub_14028668C.md)

## Referenced by

- Called by: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md), [sub_14022F868](sub_14022F868.md)
- Observed behaviours: [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md)

## Open questions

I: the callers' purpose (picking a job to show for a secondary skillset).
