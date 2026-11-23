# SceneTaskDispatch

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the opening and title scenes advance. Scene_Init resets the scene globals and enters one of the two start scenes; one of the two scene loops then runs a single task handler per frame. The current handler is the table entry selected by the id at the top of the task stack, and handlers move the scene on by changing that stack.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 | [Scene_Init](../functions/Scene_Init.md) | V | Resets the scene globals, clears the task-stack depth to 0 and calls TitleScene_Start when its mode argument is non-zero, else OpeningScene_Start. The start function pushes the first id: 14 for the title scene, 0 for the opening scene. |
| <a id="1"></a>1 | [SceneLoop_Run](../functions/SceneLoop_Run.md) | V | Calls Scene_Init, then loops while bit 0 of dword_141876EE8 is set. Each pass dispatches tbl_OpeningTaskSteps[dword_1418772E0[dword_141877480 - 1]](). |
| <a id="2"></a>2 | [SceneLoop_RunAlt](../functions/SceneLoop_RunAlt.md) | V | Does not call Scene_Init: it seeds the same globals itself, pushes task id 9, then runs the same per-frame dispatch loop while bit 0 of dword_141876EE8 is set. |
| <a id="3"></a>3 | [SceneLoop_Run](../functions/SceneLoop_Run.md) | V | A handler advances the scene by editing the stack. TitleScene_Task (14) replaces the top id with 15, 13 or 11; OpeningScene_Resume (13) pops and re-enters OpeningScene_Start. On the next pass the loop dispatches the new top id. |

## Behavior

- V: both loops use the same table and the same stack read; the only difference at the dispatch site is the loop around it.
- V: the id is dword_1418772E0[dword_141877480 - 1], the last id pushed. The loop does not use a handler's return value to choose the next task; it always reads the stack again.
- V: Scene_Init does not push a task itself. It zeroes the depth and calls TitleScene_Start (mode non-zero, pushes 14) or OpeningScene_Start (mode 0, pushes 0).
- V: SceneLoop_Run calls Scene_Init first; SceneLoop_RunAlt does not, and it starts at id 9 instead of the ids the start functions push.
- I: the scene advances as a small stack machine: a handler either replaces the top id or pops, and the next frame reads the new top (rests on the push and pop sites read in the handlers and on the loop always reading depth - 1).

## Notes

Covers Scene_Init, both scene loops and the table, plus the handlers named in the steps. The first task is pushed by TitleScene_Start / OpeningScene_Start, not by Scene_Init; those two start functions are covered only around their push. TitleScene_Task and OpeningScene_Resume are mentioned as text; their own pages carry the detail.

## Open questions

? what task 9 (SceneLoop_RunAlt's first id) does; ? how ids 2, 8 and 12 enter the stack (no store of those ids was found); ? whether every handler path leaves the depth at 1 or more.
