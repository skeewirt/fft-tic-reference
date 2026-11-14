# JobListBuilderCallersHold24Words

- **Kind:** observed behaviour
- **Scope:** engine (job list consumers)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobList_BuildForPartyUnit](../functions/JobList_BuildForPartyUnit.md), [Unit_CollectJobSkillsets](../functions/Unit_CollectJobSkillsets.md), [Unit_CollectJobSkillsetPairs](../functions/Unit_CollectJobSkillsetPairs.md), [JobScreen_FillUnitRows](../functions/JobScreen_FillUnitRows.md), [JobChange_FillUnitEntry](../functions/JobChange_FillUnitEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

JobList_BuildForPartyUnit is called by seven functions and each hands over a buffer sized for the stock list (24 words, 48 bytes); only the Jobs screen's own call uses the 48-word g_RuntimeJobList.

## Behavior

- V (decompiled frames): Unit_CollectJobSkillsets, Unit_CollectJobSkillsetPairs and sub_14028A8B0 each build into a local array of 24 words; sub_1400DCFE4 builds into word_143CDAAE0, an object of 48 bytes followed by dword_143CDAB10; JobScreen_FillUnitRows builds into word_14375F800, 48 bytes before word_14375F830.
- V: JobList_BuildForPartyUnit callers (xrefs): sub_1400DCFE4, Unit_CollectJobSkillsets, Unit_CollectJobSkillsetPairs, sub_14028A8B0, JobScreen_FillUnitRows, JobChange_FillUnitEntry, JobTree_FillJobRecords; JobList_Build is also called by sub_14028668C.
- ?: JobChange_FillUnitEntry's buffer size (a local of its frame) was not measured.

## Open questions

None recorded.
