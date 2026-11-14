# PartyUnitRecord

- **Kind:** structure
- **Area:** [Unit data](../areas/unit-data.md)
- **Size:** 640 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A unit as the party, status and job screens read it (55 records at g_PartyUnitRecords, reached through g_PartyUnits). Same per-job arrays as the save record at other offsets.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="job"></a>`0x24` | job | `uint16` | V | Current job id. |
| <a id="save_slot"></a>`0x2C` | save_slot | `uint16` | V | The save record index (PartyUnit_WriteBackToSave writes back into g_UnitSaveData[save_slot] when it is below 54). |
| <a id="marker"></a>`0x72` | marker | `uint8` | V | The unit marker (save record +0). |
| <a id="unlock_mask"></a>`0x78` | unlock_mask | `uint8[3]` | V | Unlock bits (the job list builder reads them with the bit reader). |
| <a id="learned"></a>`0x7B` | learned | `uint8[66]` | V | Learned-ability bits, 3 bytes per job index. |
| <a id="job_levels"></a>`0xBD` | job_levels | `uint8[12]` | V | Job level nibbles. |
| <a id="jp"></a>`0xCA` | jp | `uint16[23]` | V | Current JP per job index (JobMenu_ReadJp, Unit_SpendJp). |
| <a id="total_jp"></a>`0xF8` | total_jp | `uint16[23]` | V | Total JP per job index. |

## Behavior

- V: PartyUnit_FillFromWork builds it from a work record and a save record; PartyUnit_WriteBackToSave copies the arrays back.

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
