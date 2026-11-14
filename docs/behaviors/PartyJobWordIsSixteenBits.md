# PartyJobWordIsSixteenBits

- **Kind:** observed behaviour
- **Scope:** engine (party and save records, Jobs screen)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md), [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The party record's 16-bit job word (+0x24) carries a job id above 255 through the Jobs screen, the status header and the skillset lookup; only the save record's byte (+2) cannot.

## Behavior

- V: rebuilding the party record from the save record (leaving and re-entering Status) puts the save byte back into the word.
- V: a job list entry above 1023 needs the mask at the start of JobTree_FillJobRecords (3FF) widened.
- I: nothing else was seen reading the party word as a table index; the readers that only compare the id (the 9 sites of the research census) were not each exercised.

## Open questions

None recorded.
