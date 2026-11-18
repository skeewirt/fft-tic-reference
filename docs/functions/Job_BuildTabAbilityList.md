# Job_BuildTabAbilityList

- **Address:** `0x14028A400`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `uint16 *Job_BuildTabAbilityList(uint16 job, int tab, uint8 unitFlags, uint16 defaultSkillset)`
- **Callers:** JobScreen_BuildJobTabRows, sub_14028ACD8
- **Callees:** Skillset_BuildTabAbilityList

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The tab-filtered ability list of a job's skillset (its JobTable row byte 0), or of `defaultSkillset` when no row holds that skillset.

## Behavior

- V: the job's row is read when job < the bound (0xAE stock), else through a null pointer.
- V: then searches the first row (0 up to the same bound) whose skillset equals the job's: found -> that skillset, not found -> defaultSkillset; tail-calls Skillset_BuildTabAbilityList(skillset, tab, unitFlags).

## State touched

- Calls: [Skillset_BuildTabAbilityList](Skillset_BuildTabAbilityList.md)

## Referenced by

- Called by: [JobScreen_BuildJobTabRows](JobScreen_BuildJobTabRows.md), [JobScreen_BuildLearnableList](JobScreen_BuildLearnableList.md)
- Reads tables: [JobTable](../tables/JobTable.md)

## Notes

None recorded.

## Open questions

None recorded.
