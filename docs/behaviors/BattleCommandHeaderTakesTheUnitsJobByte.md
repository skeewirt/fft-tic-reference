# BattleCommandHeaderTakesTheUnitsJobByte

- **Kind:** observed behaviour
- **Scope:** engine (battle Abilities list)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The header of the battle Abilities list (the job name and icon above the commands) is a job record built by sub_140335140: for the unit's own job command it takes the battle unit's job byte (+3); for a secondary command the job that owns the command's skillset.

## Behavior

- V (decompiled): with the command index 1 the job is the unit record's +3; otherwise UnitWork_FindJobBySkillset(unit, command); JobRecord_FromJobId then builds the header record.
- V (seen live): the header names the job of the selected command.

## Open questions

None recorded.
