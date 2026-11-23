# BattleTask_Slot13Entry

- **Address:** `0x140229D24`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `_QWORD *BattleTask_Slot13Entry(void)` (returns what `Battle_UnitStatusFillAlt` returns)`
- **Callers:** scene task table, program records 2, 3 and 6 (via `BattleAction_RunScript`); `sub_1402C7DAC` references it at 0x1402C7DC0 (not examined)
- **Callees:** `sub_140226E44`, `Battle_UnitStatusFillAlt` (tail jump at `0x140229D7C`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One battle scene task, started as slot 13 by the battle program records 2, 3 and 6: refreshes scene state, seeds the
panel counters and hands the slot to the mode-0 (actor-side) variant of the alternate battle unit status panel, which
then runs until the panel closes. Whether any of this is specific to Wait is **not** established: the live
observation of the scene slot going 0 -> 13 -> 0 after choosing Wait was the scene-task scheduler's round-robin
cursor (`dword_140D40948`) cycling, not a Wait marker (turn-engine review). The task computes no damage and no turn
owner.

## Behavior

- V: calls `sub_140226E44` at `0x140229D28` (scene/UI refresh; it refills the two status-panel stat blocks from the
  preview units).
- V: sets `word_1408082D0 = 2`, or `0xC00` when bit 15 of the word read through `a0_5` is set (that test comes after the
  counters are cleared and reads `a0_5`, not `word_142FF3CA8`). The address lies inside the mode-0 number table at
  `0x140808200` (record 6, the `at` field); what the word controls there is not established.
- V: clears `word_142FF3CA8` and sets `word_142FF3CAC = 1` (`0x140229D42`/`0x140229D4C`); the panel task advances
  both counters again once it runs.
- V: tail-jumps `Battle_UnitStatusFillAlt(&word_1408081E0, 0, &a4_0[2], &unk_1407832A0)` at `0x140229D7C`, i.e.
  the mode-0 number table at `0x140808200` (the unnamed fourth table) and the actor-side stat block. Mode 0 is
  the actor-side panel variant: the routine fills the panel's attribute record, places its sprite cells, draws ten
  number fields into two staging buffers and keeps redrawing once a frame until the task's close word is set, then
  calls `SceneTask_Terminate` at `0x1402290AE`. It is a status-panel task, not a message runner.
- V: the message/banner role belongs to the sibling task `sub_140227558`, which records 2 and 3 start as slot 10 with
  tag 16, not to this entry.
- V: the three program records start this entry as the last of four task slots (slot 13): records 2 and 3 give it tag
  17, record 6 gives it tag 37. Record 3 adds `sub_14022A19C` in slot 11, and record 6 runs this entry beside that
  same task.
- V: no formula call, no result record write and no turn-owner write in this function.
- I: the next unit is selected by the CT/turn engine (C2); this task only closes the presentation.

## State touched

- Calls: [sub_140226E44](sub_140226E44.md), [Battle_UnitStatusFillAlt](Battle_UnitStatusFillAlt.md)

## Notes

Record 2 (`{sub_140227558, -, -, this}`) is only a candidate for the Wait program, by elimination: it adds no message
task, unlike record 3. Record 2 is also started by the turn-start state (`sub_140209218` case 2), so the same
task may cover both "wait for command" and "end turn"; live check needed.

Corrected 2026-11-22: the earlier sheet called `sub_140228778` "the battle message/event runner". That function is
`Battle_UnitStatusFillAlt`, the alternate status panel; slot 13 runs its mode-0 (actor-side) variant. The message
and banner work in these programs is the separate `sub_140227558` task. The scheduler findings above were kept.

## Open questions

- Is this the Wait-specific task or the generic turn-end task? Statics cannot separate the two.
