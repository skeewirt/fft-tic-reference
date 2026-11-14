# ScriptedBattleUnitsFromEntries

- **Kind:** flow
- **Area:** [Job data](../areas/job-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a scripted battle gets its units: the battle key picks 16 entries, the OverrideEntryData rows of the key overwrite them in place, and battle unit i is built from entry i with row i.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [sub_1403044EC](../functions/sub_1403044EC.md) | V | Battle load state 4: the key dword of g_BattleEntrySource = scene variable 50; state 5 calls Battle_BuildEntryUnits. |
| <a id="2"></a>2 | [Battle_GetEntryBlock](../functions/Battle_GetEntryBlock.md) | V | The 640-byte block of the key in the loaded entry data (null for key 0). |
| <a id="3"></a>3 | [OverrideEntry_LoadBattleEntries](../functions/OverrideEntry_LoadBattleEntries.md) | V | Only when the dword at 0x1407D453C is not 0: for index 0..15 the row (key, index) of OverrideEntryData, its pointer into rows[index], OverrideEntry_FillUnitEntry into entry index. |
| <a id="4"></a>4 | [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md) | V | For i = 0..15 with a non-zero entry byte 0: g_CurrentSpawnEntry = entry i and Unit_BuildFromRecord(g_PreviewUnitTable + 512 x i, entry i, 0, 0, rows[i]). |
| <a id="5"></a>5 | [Unit_BuildFromRecord](../functions/Unit_BuildFromRecord.md) | V | Unit_ApplySpawnRecord (marker, level, birthday, brave / faith; +2 = 0xFF for a unit without a save record), then UnitWork_InitFromSpawnRecord(c, entry, row). |
| <a id="6"></a>6 | [UnitWork_InitFromSpawnRecord](../functions/UnitWork_InitFromSpawnRecord.md) | V | Levels and unlock mask, job byte +3 = entry +10, UnitWork_ApplyJobRow(c, row), whose sub_1401EA910 adds the row's HP / MP growth bonuses. |
| <a id="7"></a>7 | [LookQueue_Add](../functions/LookQueue_Add.md) | V | Back in Battle_PlaceEntryUnits: every kept unit's look is queued. |

## Open questions

? what sub_1402F3A04 does with the entry base after step 4; ? the other caller sub_14030476C's battle mode.
