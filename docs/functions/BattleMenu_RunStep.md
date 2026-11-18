# BattleMenu_RunStep

- **Address:** `0x1402381C4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleMenu_RunStep(void)`
- **Callers:** sub_140238360
- **Callees:** SceneTask_Start, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one step of the battle menu step table: sets the current menu and starts the step's task.

## Behavior

- V: the step id comes from the scene task block; with option bits 0x18000 set it is replaced by the step's alternate id (+24).
- V: waits until the previous task and a busy test are done, then copies the step's menu id, screen code, auxiliary word and flag into the menu node and globals.
- V: step 31 first starts a fixed task; every step then starts its own task function (+16) in slot 8.

## State touched

- Calls: [SceneTask_Start](SceneTask_Start.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Open questions

None recorded.
