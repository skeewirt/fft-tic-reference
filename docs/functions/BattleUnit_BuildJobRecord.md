# BattleUnit_BuildJobRecord

- **Address:** `0x1400FCF80`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `void BattleUnit_BuildJobRecord(unsigned int slot, JobRecord *out)`
- **Callers:** Battle_UnitStatusFill, Battle_TimelineRefresh, Battle_UnitStatusFillAlt, sub_1402DF374
- **Callees:** JobRecord_FromJobId

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 148-byte job record of battle unit `slot` for the battle panels: its job, levels and JP, through JobRecord_FromJobId.

## Behavior

- V: for slot 0..20 the unit is g_PreviewUnitTable + 512 x slot; the job byte +3 is loaded at 0x1400FCFC9 and becomes the record's job id.
- V: the 12 level bytes (+228), the 46 JP bytes (+240) and the 46 total JP bytes (+286) are copied into its own frame; in the first 20 words of the JP and total JP copies a value of 10000 or more becomes 9999; the source then points at these copies, with the unit's flags +6.
- V: JobRecord_FromJobId(out, source) fills the record (name, level, JP).

## State touched

- Calls: [JobRecord_FromJobId](JobRecord_FromJobId.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Referenced by

- Called by: [Battle_TimelineRefresh](Battle_TimelineRefresh.md), [Battle_UnitStatusFillAlt](Battle_UnitStatusFillAlt.md), [sub_1402DF374](sub_1402DF374.md)
- Observed behaviours: [BattlePanelJobLineShowsDashesAtLevelZero](../behaviors/BattlePanelJobLineShowsDashesAtLevelZero.md), [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md)

## Notes

The level, JP and total JP copies in this frame cover the stock job entries only; a job index beyond them would address past the copies.

## Open questions

None recorded.
