# UnitJobFlags

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable (filled at run time)
- **Address:** `0x1411A7490`
- **Rows:** 1 block of 146 bytes (21 + 125 flag bytes)
- **Keyed by:** bytes 0..20 generic job index; bytes 21..145 job type 0..124 (+21)
- **Read by:** [GameState_ResetJobFlags](../functions/GameState_ResetJobFlags.md), [JobList_RecomputeAvailability](../functions/JobList_RecomputeAvailability.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md), [SaveJobNew_Serialize](../functions/SaveJobNew_Serialize.md)
- **Held in:** [g_UnitJobFlags](../globals/g_UnitJobFlags.md)
- **Row layout:** [UnitJobFlagsBlock](../structs/UnitJobFlagsBlock.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The job flag block: 21 per-job "new" flags and 125 per-job-type disable flags. Reset for a new game, recomputed from the party whenever the job list is rebuilt, and saved in the save file as its own two-field record.

## Behavior

- V: the new-game reset writes 1 into every one of the 125 type flags, and for each of the 21 job flags writes 1 when a byte of the matching generic job NXD row is zero.
- V: JobList_RecomputeAvailability clears a type flag for the job type of every party unit current job, and again for each generic job a unit has unlocked (unlock bit of that job index) when that job row has a type.
- I: a type flag of 1 therefore means no party unit has that job type yet (the list code treats it as not yet owned).
- V: the type index comes from job table row +24 and is bounded by 125; the 21 job flags are read by the job tree and job screen code.

## Notes

Our names. Saved record: SaveJobNew_Serialize, a 21-entry array (each entry a one-byte flag) then a 125-byte array.

## Open questions

- ?: the exact player-visible effect of a job flag of 1 (the badge shown on a job)
- ?: which column of the generic job NXD row the new-game reset tests
