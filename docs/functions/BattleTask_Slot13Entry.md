# BattleTask_Slot13Entry

- **Address:** `0x140229D24`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t BattleTask_Slot13Entry(void)`
- **Callers:** scene task table, program records 2, 3 and 6 (via `BattleAction_RunScript`)
- **Callees:** `sub_140226E44`, `sub_140228778` (tail jump)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One battle scene task, started as slot 13 by the battle program records 2, 3 and 6: refreshes scene state and runs the battle
event/message runner that ends the task. Whether any of this is specific to Wait is **not** established: the live observation of the
scene slot going 0 -> 13 -> 0 after choosing Wait was the scene-task scheduler's round-robin cursor (`dword_140D40948`) cycling, not a Wait
marker (turn-engine review). The task computes no damage and no turn owner.

## Behavior

- V: calls `sub_140226E44` at `0x140229D28` (scene/UI refresh).
- V: sets `word_1408082D0 = 2`; when `word_142FF3CA8` has bit 15 set, sets it to `0xC00` instead
  (`0x140229D55`).
- V: clears `word_142FF3CA8` and sets `word_142FF3CAC = 1` (`0x140229D42`/`0x140229D4C`).
- V: tail-jumps `sub_140228778(&word_1408081E0, 0, &a4+4, &unk_1407832A0)` at `0x140229D7C`; that
  routine is the battle message/event runner and calls `SceneTask_Terminate` at `0x1402290AE`.
- V: no formula call, no result record write and no turn-owner write in this function.
- I: the next unit is selected by the CT/turn engine (C2); this task only closes the presentation.

## State touched

- Calls: [sub_140226E44](sub_140226E44.md)

## Notes

Record 2 (`{sub_140227558, -, -, this}`) is only a candidate for the Wait program, by elimination: it adds no message task,
unlike record 3. Record 2 is also started by the turn-start state (`sub_140209218` case 2), so the same
task may cover both "wait for command" and "end turn"; live check needed.

## Open questions

- Is this the Wait-specific task or the generic turn-end task? Statics cannot separate the two.
