# Job_HasMonsterPair

- **Address:** `0x1402CBF60`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `bool Job_HasMonsterPair(unsigned int jobId)`
- **Callers:** (see xrefs)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when the Job row's poach_item (+0x24) or poach_item_rare (+0x28) is nonzero: the job can be poached. The function name says 'monster pair'; that reading was wrong, the two values are the PoachItem ids a Poach on a unit of the job can give.

## Behavior

- V: reads the Job row (table 46) and returns 1 when the dword at +0x24 or the dword at +0x28 is nonzero, else 0 (also 0 when the table or the row is missing).
- V: Poach_GiveResult is the reader that uses the two values as PoachItem ids (see its sheet); nothing in this function treats them as sprites or portraits.

## Referenced by

- Called by: [sub_1403067D0](sub_1403067D0.md)
- Observed behaviours: [PoachResultFromJob](../behaviors/PoachResultFromJob.md)

## Notes

M: in stock the values are nonzero only for the jobs that can be poached (monster jobs); the name Job_HasMonsterPair is the old reading and stays only because it is the name applied in the executable database.

## Open questions

None recorded.
