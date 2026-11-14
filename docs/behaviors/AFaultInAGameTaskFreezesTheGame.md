# AFaultInAGameTaskFreezesTheGame

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Application and startup](../areas/app-startup.md)
- **Affects:** [GameTasks_RunFrameSteps](../functions/GameTasks_RunFrameSteps.md), [SceneTask_WaitFrame](../functions/SceneTask_WaitFrame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Game logic runs in task threads that the main thread hands control to each frame (GameTasks_RunFrameSteps waits on them). A fault inside a task kills that thread without a crash: the main thread waits forever, the pad is no longer polled, and no dump is written.

## Behavior

- V (live 2026-11-10): an access violation in a scene task (sub_14030DD8C) froze the game on the deployment screen; the main thread sat in WaitForSingleObject inside GameTasks_RunFrameSteps, every task thread was parked in its wait, the pad poll count stopped, and Windows wrote no crash dump.

## Open questions

? where the task's fault is swallowed (a handler of the task runner).
