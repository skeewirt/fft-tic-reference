# RuntimeJobList

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable (filled at run time)
- **Address:** `0x143C51890`
- **Rows:** 48 rows of 2 bytes
- **Keyed by:** list position
- **Read by:** [JobList_IsSelectedEntryUnflagged](../functions/JobList_IsSelectedEntryUnflagged.md), [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md)
- **Held in:** [g_RuntimeJobList](../globals/g_RuntimeJobList.md)
- **Row layout:** [RuntimeJobListEntry](../structs/RuntimeJobListEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Change Job list the game builds each time the job screen fills; the list length is a separate int16 at 0x143C510D8.

## Behavior

- V: rebuilt on every fill, so a stored value has no lasting effect.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
