# g_BattleEntrySource

- **Kind:** global
- **Address:** `0x141856930`
- **Area:** [Unit data](../areas/unit-data.md)
- **Type:** `unit data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

16 bytes: dword +0 the battle key (set from scene variable 50 by BattleLoad_StepFresh, read by Battle_GetEntryBlock and Battle_BuildEntryUnits as the OverrideEntryData key), qword +8 the base of the loaded entry data (640 bytes per battle). Battle_RestoreSceneVars restores all 16 bytes from the battle snapshot (0x140897DB8), so after a resume the key is the saved battle's and the pointer the saving process's

## Referenced by

- Read by: [Battle_BuildEntryUnits](../functions/Battle_BuildEntryUnits.md), [Battle_GetEntryBlock](../functions/Battle_GetEntryBlock.md)
- Written by: [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md)

## Open questions

None recorded.
