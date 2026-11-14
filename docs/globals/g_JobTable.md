# g_JobTable

- **Kind:** global
- **Address:** `0x140785E30`
- **Area:** [Job data](../areas/job-data.md)
- **Type:** `uint8[174][49]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The stock job table: 174 rows of 49 bytes. The first byte is the skillset, the later bytes carry growth, statuses, elements and the two script bytes 46 and 47.

## Behavior

- V: addressed as row times 0x31 by the job readers, the party job-record builder and the job screen.

## Referenced by

- Described by tables: [JobTable](../tables/JobTable.md)
- Read by: [BattleCommand_BuildScreen](../functions/BattleCommand_BuildScreen.md), [JobScreen_BuildLearnList](../functions/JobScreen_BuildLearnList.md), [JobScreen_FillUnitRows](../functions/JobScreen_FillUnitRows.md), [JobScreen_RefreshLearnList](../functions/JobScreen_RefreshLearnList.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [UnitWork_BuildForSlot](../functions/UnitWork_BuildForSlot.md), [Unit_BuildInnateStatuses](../functions/Unit_BuildInnateStatuses.md)

## Open questions

None recorded.
