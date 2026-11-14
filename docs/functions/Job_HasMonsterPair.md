# Job_HasMonsterPair

- **Address:** `0x1402CBF60`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `bool Job_HasMonsterPair(unsigned int jobId)`
- **Callers:** (see xrefs)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when Job row +36 or +40 (Unknown10 / Unknown11) is nonzero: the job has a monster sprite/portrait pair.

## Behavior

- V: inlined Job getter, returns 1 if either dword is nonzero.

## Referenced by

- Called by: [sub_1403067D0](sub_1403067D0.md)

## Notes

I: stock nonzero only for monster jobs 94..141 / 169..173.

## Open questions

None recorded.
