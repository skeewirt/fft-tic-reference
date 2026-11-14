# BattleAction_RunScript

- **Address:** `0x140234B3C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void __noreturn BattleAction_RunScript(void)`
- **Callers:** `BattleAction_StartScript` (`SceneTask_Start(2, ...)`), the scene task table
- **Callees:** `SceneTask_Start`, `SceneTask_WaitFrame`, `SceneTask_Terminate`, `memset`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The driver task for the battle presentation programs: reads the current script id from scene block 1,
starts up to four sub-tasks defined by that script's 64-byte record, waits for them and repeats, then
ends.

## Behavior

- V: script id = `dword[off_140783088 + 0x800 * currentSlot]` (block 1 offset 0); stores it in
  `dword_140D4094C`.
- V: record = `0x140672210 + (id << 6)`; layout `{void *func[4] at +0, uint32 taskSlot[4] at +32,
  uint32 tag[4] at +48}`.
- V: for each of the four entries with `func != -1` and a free task slot, calls
  `SceneTask_Start(taskSlot[i], func[i])` at `0x140234CF6`; writes `tag[i]` into the task block at
  `+0x98`; marks the entry as started (local state 2).
- V: after starting, waits (`SceneTask_WaitFrame` at `0x140234CE0`) until a started task's tag differs
  or the task ended, then restarts the remaining entries at `0x140234D5F`.
- V: the loop ends when the block's first qword is 255; then `SceneTask_Terminate`.
- V: record 0 is empty (all `func = -1`), records 1..6 are the live programs (see
  `docs/reference/battle-actions.md`).

## State touched

- Calls: [SceneTask_Start](SceneTask_Start.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Notes

The tags let the event script wait for a program kind (`SceneTask_FindTag`), e.g. tag 21 for the action
message task.

## Open questions

- What the "wait for a different tag" condition is used for (interrupting a running program).
