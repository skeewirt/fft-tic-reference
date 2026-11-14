# JobScreenFrame

- **Kind:** flow
- **Area:** [Job tree](../areas/job-tree.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the Job Tree gets input and a chance to run code each frame: the party-menu scene's frame function runs the current screen's update through a function table, the job screen's update runs the screen dispatch, and that dispatch calls JobTree_HandleInput while the tree has the input focus (1409).

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [sub_1402BBBCC](../functions/sub_1402BBBCC.md) | I | A scene frame function (the existing sheet names it the equip confirm path): when byte_1407DC4AA is set it calls funcs_14020F527[dword_141811424]() once per pass, then reads the screen state at g_CharaRenderMgr+13452. Callers: four per-scene frame wrappers (sub_1402BC388, sub_1402C2EBC, sub_1402C30C8, sub_1402C334C). |
| <a id="2"></a>2 | [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md) | V | Entry 3 of the function table at 0x1406806C0 (0x1406806D8 holds the thunk j_JobScreen_UpdateState). Its tail runs the screen dispatch with the focus id from g_CharaRenderMgr+13452 (states 1400 .. 1412). |
| <a id="3"></a>3 | [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md) | V | sub_140115EA8, the job screen's dispatch (no sheet): focus 1409 sends the call to JobTree_HandleInput(tree addon, outCode); any other focus goes to the job list addon (sub_14012E82C). |
| <a id="4"></a>4 | [JobTree_HandleInput](../functions/JobTree_HandleInput.md) | V | Confirm, cancel, then the eight direction bytes; the call is at 0x140115F0F and runs every frame the tree has the focus. |
| <a id="5"></a>5 | [GUINode_SetPosition](../functions/GUINode_SetPosition.md) | V | Moving the tree root (the scroll) marks it dirty; GUINode_UpdateSubtree re-derives every child matrix in the same UI pass. |

## Behavior

- I: that the table entry runs once per frame was not counted (the call sits in a per-pass function); the live check is a counter at the call of step 4 against a one-second timer.
- V: the UI frame time is g_GUICore+2100 (GUICore_BeginFrame), the value the stick-driven code of this build multiplies its step by.

## Referenced by

- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Open questions

? how many times per second step 4 runs while the tree is focused (expected 60).
