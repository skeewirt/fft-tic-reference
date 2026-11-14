# BTurn_OnTurnStartStatus

- **Address:** `0x14030F9A0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int __fastcall BTurn_OnTurnStartStatus(int ct, uint8_t *unit)`
- **Callers:** `Battle_TurnEngine` (`0x14030F40E`)
- **Callees:** `sub_14030A410`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the per-turn status roll at the moment a unit is selected (after `CT % 100`): decides whether the turn is
consumed by a status and queues the pending status effects for the action block at `unit + 0x1BE`.

## Behavior

- V: computes one LCG step (`xmmword_1408E5FC8`) for the random rolls.
- V: if `unit[0x61] & 0x30 == 0x20` and `unit[0x63] & 0x20` is set: sets damage = `max HP / 10` (minimum 1),
  effect bytes `+0x1BE+8`, `+34`, `+36 = 32`, and returns 2.
- V: when the unit is not being simulated (`g_BattleSimulating == 0`) and `unit[0x61] & 0x20 == 0`, it applies the
  pending status counters: `unit[0x75]` countdown, `unit[0x61] & 2` -> effect byte 2, `unit[43] < 10` -> poison-like
  flag, and returns 1 when any pending status was set.
- V: when the status is "sleep/stop-like" (`unit[0x61] & 0x10`) and the RNG is odd, returns 2 with a queued effect.
- V: the caller treats a non-zero result with bit 0 set as "consume the turn now" (`Battle_TurnEngine` returns
  `slot | 0x300`); a result of 2 lets the turn start normally with the effect queued.

## Referenced by

- Called by: [Battle_TurnEngine](Battle_TurnEngine.md)
- Observed behaviours: [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md), [KoLeavesSomeStatusesOnTheUnit](../behaviors/KoLeavesSomeStatusesOnTheUnit.md)

## Notes

The first argument (the CT remainder) is passed but not used in the paths read; the rolls come from the global LCG.
The Reraise test reads the effective status set.

## Open questions

The exact status ids behind `unit[0x61] & 0x20` / `& 0x10` and the effect encoding at `+0x1BE` (C1/C4 territory).
