# JobIdSpace

- **Kind:** registry
- **Area:** [Job data](../areas/job-data.md)
- **Resolved by:** [Job_IdToIndex](../functions/Job_IdToIndex.md)
- **Values stored in:** [UnitSaveRecord.job](../structs/UnitSaveRecord.md#job)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What a job id (the byte in save record +2 and work record +3) means to the code, and the job index the per-job arrays use for it.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="ids 0..73"></a>0 | `ids 0..73` | `index 0 (Job_IdToIndex default)` | V | Story and special characters: their own JobTable rows; the per-job arrays are read at index 0 when code asks. |
| <a id="ids 74..93"></a>74 | `ids 74..93` | `index id - 74 (0..19)` | V | The 20 generic jobs (74 Squire ... 93 Mime). |
| <a id="ids 94..159"></a>94 | `ids 94..159` | `index 0` | V | Monsters (the range tests treat >= 94 as a monster). |
| <a id="ids 160, 161"></a>160 | `ids 160, 161` | `index 20, 21` | V | Unused stock slots (Dark Knight / Onion Knight in older releases). |
| <a id="ids 162..173"></a>162 | `ids 162..173` | `index 0` | V | Special ids (0xA2..0xA4 tested by the code) and blank rows. |

## Open questions

None recorded.
