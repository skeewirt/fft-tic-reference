# Battle_AITurnRun

- **Address:** `0x14038A468`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall Battle_AITurnRun()`
- **Callers:** `Battle_AITurnPrepare` (`0x14031F534`), `sub_140320C4C`, `sub_14038A410`, `sub_14038E120`
- **Callees:** `sub_14038B104`, `sub_14038AED4`, `sub_140281434`, `sub_14038AB28`, `sub_14038AA68`, `sub_140279370`, `BTurn_FinishUnit`, `Battle_TurnEngine`, `sub_14030A488`, `sub_14038BB68`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one AI trial: applies the candidate action on the preview unit table, lets the turn engine play on (up to 255
steps), scores the outcome and restores the engine state.

## Behavior

- V: saves `dword_14186B040`, `dword_14186B044` and `dword_1407B0708` before running and restores them on abort
  (`LABEL_53`).
- V: loops `Battle_TurnEngine(0)` up to 255 times (`word_141872594`).
- V: code `0x300` -> `sub_14030A488(slot)` (end-of-turn effects).
- V: code `0x200` -> `sub_14038AB28` validates the pending action; on success it clears `unit[0x61]` bits 1/3,
  `unit[0x1EF]` bits 1/3 and `unit[0x18D] = -1` (the charge resolves); on failure it restores the engine state and
  returns 0.
- V: code `0x100` -> `sub_14038BB68(0, slot)` scores the plan, sets the AI table byte `xmmword_1418724B8+slot = 1`,
  and clears `unit[0x1B8]` so the engine can finish the turn.
- V: the tail of the function scores the simulated outcome (it does not choose; the planner compares the scores): for
  each unit, HP x 128 / max HP, plus `tbl_AiStatusValue[s]` (0x1407B22F0) for each status s of 0..39 the unit has
  (Blindness and Silence scaled by a per-unit AI byte / 4; Confusion, Vampire and Charmed halved under some conditions;
  some statuses counted only under conditions), plus an MP term and 51 for each of 7 words of the unit (+0x1A..) that equals a word the AI stored at qword_141873070 (? their meaning); units of the
  acting side add, the others subtract; the total is kept in the high word of `dword_1418716D0`.
- V: it uses `sub_140279370` (facing/pose) when the chosen action needs one.

## State touched

- Calls: [BTurn_FinishUnit](BTurn_FinishUnit.md), [Battle_TurnEngine](Battle_TurnEngine.md)

## Referenced by

- Called by: [Battle_AITurnPrepare](Battle_AITurnPrepare.md)
- Observed behaviours: [AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable](../behaviors/AiJudgesStatusesThroughTheFortyBitSetsAndAValueTable.md)

## Notes

Same engine as the player path; the difference is that the AI never shows the command menu and can run several engine
steps in one frame. `sub_14031F534` prepares the per-unit AI table before this runs.

## Open questions

The full scoring formula (it is a large table-driven block) and how the Auto command routes player units here.
