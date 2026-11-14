# StatusBitWritersAndTheRemovalPath

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_StatusResolve](../functions/Battle_StatusResolve.md), [Battle_StatusApply](../functions/Battle_StatusApply.md), [Battle_StatusRefresh](../functions/Battle_StatusRefresh.md), [Unit_ReinitStatusCountdowns](../functions/Unit_ReinitStatusCountdowns.md), [Unit_BuildInnateStatuses](../functions/Unit_BuildInnateStatuses.md), [Unit_ReloadFromJobRowEx](../functions/Unit_ReloadFromJobRowEx.md), [Unit_SetChargeStateBits](../functions/Unit_SetChargeStateBits.md), [sub_14030D1CC](../functions/sub_14030D1CC.md), [BTurn_PreviewAction](../functions/BTurn_PreviewAction.md), [Unit_InitBattleStatusState](../functions/Unit_InitBattleStatusState.md), [EventUnitStatus_SaveAndHide](../functions/EventUnitStatus_SaveAndHide.md), [sub_14024138C](../functions/sub_14024138C.md), [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective), [UnitWorkRecord.applied_status](../structs/UnitWorkRecord.md#applied_status)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The effective set +0x61 of a unit is written at the end of a fixed group of functions; the applied set is written only from the pending sets, from its own saved copy or derived from +0x61; the game removes a status only through the pending remove.

## Behavior

- V (code read): the writers of +0x61 in battle are the tails of Battle_StatusApply, Battle_StatusRefresh, Unit_ReinitStatusCountdowns, Unit_BuildInnateStatuses and its Ex twin, Unit_SetChargeStateBits (byte 0), sub_14030D1CC (byte 0), BTurn_PreviewAction, the clear-all branch of Battle_ApplyActionResult, the unit builders, and the whole-set copies back of the event restore and the AI.
- V (code read): the applied set is written only from the pending sets (Battle_StatusApply / Refresh), from its own saved copy (Unit_BuildInnateStatuses, the event restore) or derived from +0x61 by Unit_InitBattleStatusState, whose callers build the record just before; stock countdowns tick only for applied bits (Battle_TurnEngine phase 4).
- V (code read): the tail of Battle_StatusResolve sets +5 bit 3 and the side bits from +0x61.
- V (code read): the game removes a status only through the pending remove, which Status_FilterPendingSets cuts to applied & ~innate a.

## Open questions

None recorded.
