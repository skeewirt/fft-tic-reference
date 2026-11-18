# Battle_TurnEngine

- **Address:** `0x14030F030`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int __fastcall Battle_TurnEngine(int reset)`
- **Callers:** `Battle_TurnStep` (`0x1402029DC`, call at `0x1402029E8`), `BattleLoad_StepFresh` (`0x140304712`), `sub_14030476C` (`0x140304997`), `Battle_AITurnRun` (`0x14038A468`)
- **Callees:** `sub_14002630C`, `sub_14030A410`, `Status_FilterPendingSets`, `BTurn_StatusFlags`, `BTurn_OnTurnStartStatus`, `sub_14030C240`, `sub_14030C2C0`, `sub_14030D1CC`, `BTurn_IsUnitDone`, `BTurn_FinishUnit`, `AbilityAction_GetRecord`, `SceneVar_Read`, `SceneVar_Write`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle turn state machine: ticks CT, picks the next unit, starts and finishes turns, and resolves charged actions.
It returns an action code `slot | 0x100/0x200/0x300/0x400` (or `0xFF00` on the loop guard) that the caller interprets.

## Behavior

- V: `reset != 0` clears `dword_14186B044` (phase), sets `dword_1407B0708 = -1`, clears the four per-team words at
  `0x14186B020`, the per-team arrays at `0x14186AFA0`/`0x14186B000`, per-unit state (`+0x1B8`, `+0x1E8`, `+0x1BA`)
  and `g_BattleSimulating`, then returns `0xE000` (`0x14030F0C0`-`0x14030F103`).
- V: phases are dispatched from `dword_14186B044` at `0x14030F126`: 0 tick, 1 select, 2 pending-action countdown,
  3 pending-action ready, 4 status counters, 5 build finished table, 6 pop finished unit, 9 battle start,
  10 active-unit wait, 13/14/15/17/19 clean-up.
- V: phase 0 (`0x14030F46C`): for every unit with `BTurn_StatusFlags & 1 == 0`,
  `CT = min(CT + speed, 0xFE)` with speed `+0x40`, halved on Slow (`flags & 0x20`) and x1.5 on Haste (`flags & 0x10`).
- V: phase 1 (`0x14030F349`): picks the highest CT `> 99` (ties to the lowest slot), or the unit with dword
  `+0x1F8 & 0x400`; sets the winner's CT to `CT % 100` (255 -> 0), clears the extra-turn bit, sets `+0x1B8 = 1`,
  `+0x2E = 1`, `+0x1BA = 0`, sets phase 10 and `dword_1407B0708 = slot`, returns `slot | 0x100`.
  A unit with `+0x61 & 4` is skipped with CT forced to 99.
- V: phase 9 (`0x14030F4C8`) is the first turn: highest CT without the 100 threshold (initial CT is 1..99 from
  `Unit_ApplySpawnRecord`), then the same turn-start writes and `slot | 0x100`.
- V: phase 3 returns `slot | 0x200` when a unit's `+0x18D` pending-action timer is 0; phase 6 returns `slot | 0x300`
  for units in the finished table; phase 10 returns `slot | 0x100` while the active unit is not done and finishes it
  when `BTurn_IsUnitDone` is true (`0x14030F776`-`0x14030F7A9`).
- V: the internal loop guard returns `0xFF00` after 1200 steps (compare at `0x14030F7D0`, limit 0x4B0).
- I: phases 13-19 are the clean-up of the action (status application, removal, charge resolution); see C4.
- V: phase 4 (the countdown loop with the tests at 0x14030F273 / 0x14030F27D): for every unit present and not Jumping it decrements the countdown bytes +0x66.. of the statuses 24..38 whose bit is in the applied set and not in innate a (tests at 0x14030F273 / 0x14030F27D on their byte 3, +0x1F2 and +0x5A), queues the removal at 0, and runs Status_FilterPendingSets(0).
- V: phase 19 (0x14030F595): the unit whose turn ended (g_BattleActiveUnit), unless absent, Crystal, KO, Jumping (+0x61 & 0x64), Stone or Chest (+0x62 & 0x81): Battle_ResultReset, then Poison (+0x64 bit 0x80) writes HP damage = max HP >> 3 at block +6 and 0x80 at block +39, else Regen (bit 0x40) writes the heal max HP >> 3 at +8 and 0x40; a non-zero +39 returns `slot | 0x300` (the result is applied), else on to the next phase. Phase 19 sets g_BattleTurnPhase to 15 first; phases 15 (BTurn_QueueTerrainPoison) and 17 (BTurn_QueueInvisibilityEnd) jump to the same `jz` with their own result.

## State touched

- Calls: [BTurn_StatusFlags](BTurn_StatusFlags.md), [BTurn_OnTurnStartStatus](BTurn_OnTurnStartStatus.md), [sub_14030D1CC](sub_14030D1CC.md), [BTurn_IsUnitDone](BTurn_IsUnitDone.md), [BTurn_FinishUnit](BTurn_FinishUnit.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md)

## Referenced by

- Called by: [BattleLoad_StepFresh](BattleLoad_StepFresh.md), [Battle_AITurnRun](Battle_AITurnRun.md), [Battle_TurnStep](Battle_TurnStep.md), [sub_14030476C](sub_14030476C.md)
- Observed behaviours: [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md), [BattleStatChangeAndCtGainSteps](../behaviors/BattleStatChangeAndCtGainSteps.md), [PoisonAndRegenActAtTheEndOfTheUnitsTurn](../behaviors/PoisonAndRegenActAtTheEndOfTheUnitsTurn.md)

## Notes

Called once per frame by the player command path and in a loop by the AI path. It is the only writer of
`dword_14186B044` and `dword_1407B0708`.
Addresses: the conditional jump at 0x14030F634 (phase 15, the Poison / Regen result), the CT byte load at 0x14030F49C (phase 0, the CT gain) and phase 4's filter call (0x14030F29B).

## Open questions

The exact per-unit work of phases 13/14/15/17 (it overlaps the action resolution documented by C4); phase 19 is read (Poison / Regen).
