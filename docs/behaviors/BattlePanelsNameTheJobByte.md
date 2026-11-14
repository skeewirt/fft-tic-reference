# BattlePanelsNameTheJobByte

- **Kind:** observed behaviour
- **Scope:** engine (battle unit panels)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [BattleUnit_BuildJobRecord](../functions/BattleUnit_BuildJobRecord.md), [UnitWork_FindJobBySkillset](../functions/UnitWork_FindJobBySkillset.md), [BattleCommand_BuildScreen](../functions/BattleCommand_BuildScreen.md), [sub_14022F868](../functions/sub_14022F868.md), [Battle_UnitStatusFill](../functions/Battle_UnitStatusFill.md), [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle's unit panels and command screens name a unit's job from its job byte (+3) or from the first listed job whose row holds a skillset, never from a party word.

## Behavior

- V: BattleUnit_BuildJobRecord (from Battle_UnitStatusFill, Battle_TimelineRefresh, Battle_UnitStatusFillAlt and sub_1402DF374) builds the panel's job record from byte +3 (0x1400FCFC9) and frame copies of the level, JP and total JP arrays.
- V: sub_14022F868 builds job records from a battle unit's byte +3 and from UnitWork_FindJobBySkillset; BattleCommand_BuildScreen builds the command's job record from UnitWork_FindJobBySkillset.
- V: UnitWork_FindJobBySkillset scans the unit's job list (sub_14028668C) for a row holding the skillset and otherwise returns byte +3.

## Open questions

? the formation screen's job text reader (not located).
