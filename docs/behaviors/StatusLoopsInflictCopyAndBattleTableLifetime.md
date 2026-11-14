# StatusLoopsInflictCopyAndBattleTableLifetime

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_StatusResolve](../functions/Battle_StatusResolve.md), [sub_1403052DC](../functions/sub_1403052DC.md), [Battle_StatusApply](../functions/Battle_StatusApply.md), [Battle_StatusRefresh](../functions/Battle_StatusRefresh.md), [Formula_56_StatusOnlyApplication](../functions/Formula_56_StatusOnlyApplication.md), [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md), [sub_140210AF0](../functions/sub_140210AF0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The status pipeline (Battle_StatusResolve) runs a filter, a refresh and an apply loop over the status ids in order; the inflict copy of a result is read only by formula 56; the battle task clears the unit table at its start and the battle capture copies it whole.

## Behavior

- V (code read): the game's filter, refresh and apply loops visit the status ids in order; the apply loop makes a per-status filter call.
- V (code read): Formula 56 is the only reader of the inflict copy at 0x1407B07B0 (Battle_ResolveAction writes it from g_InflictRecords).
- V (code read): the battle task marks every unit slot empty at its start (sub_140210AF0); Battle_SaveCapture and Battle_RestoreCapture copy the whole unit table.

## Open questions

None recorded.
