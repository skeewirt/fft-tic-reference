# JobListScreen_GetCursorIndex

- **Address:** `0x140116100`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `int64_t JobListScreen_GetCursorIndex(UIHolder *holder)`
- **Callers:** JobScreen_UpdateState (4 sites)
- **Callees:** holder virtual slot 2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the job-change list's current cursor index through the holder object that owns the list addon.

## Behavior

- V: returns 0 when the holder's virtual slot 2 (+16) reports false or the addon pointer at holder+120 is null.
- V: when the addon's mode (addon+19008) is 9 the value is the ability row at addon+3672, otherwise the cursor cell at addon+19016.
- V: the only caller is JobScreen_UpdateState, which calls it at four sites (0x368DAA, 0x368E61, 0x368E9E, 0x368F8D) and uses the result to index g_RuntimeJobList.
- I: the result is a cell and not an entry.

## Referenced by

- Called by: [JobScreen_UpdateState](JobScreen_UpdateState.md)

## Open questions

None recorded.
