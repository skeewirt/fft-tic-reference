# UIAgent_SetState

- **Address:** `0x1401CA59C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgent_SetState(UIAgentStateMachine *machine, int state)`
- **Callers:** UIAgentFFTOSystem_StateExitGame (call 0x140182842), UIAgentFFTOSystem_StateOpenConfig (0x1401828D7), UIAgentFFTOSystem_StateCloseConfig (0x1401829A8), UIAgentFFTOSystem_vfunc_9 (0x1401827C6), UIAgentFFTOSystem_OnAddonEvent (0x140181F59), UIAgentFFTOSystem_OpenConfig (0x1401824F8), UISaveLoad_OnEvent (0x1401834AD), UISaveLoad_Open (0x1401835E1), UISaveLoad_StateLoad (0x140183AE0), sub_1401829CC, sub_140182A74, sub_140183658, sub_1401836F0, sub_14018403C and the save/load helpers sub_140176758..sub_140177FA4; 38 call sites in all
- **Callees:** indirect only: the current handler at block +0x08, the selector at +0x10, then the handler the selector returns

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Changes a UI agent's state machine: runs the current handler with phase 2 (exit), stores the new state, selects the handler for that state, and runs the new handler with phase 0 (enter). The machine is a 32-byte control block embedded in the agents that use states; System and SaveLoad place theirs at +0x48.

## Behavior

- V: the first argument is the control block, not the agent: +0x00 owner (the agent pointer), +0x08 the current handler, +0x10 the selector, +0x18 the state id. The System agent's callers pass agent +0x48, so its state id sits at agent +0x60.
- V: the current handler runs first, as handler(owner, 2) - the exit phase. The pseudocode shows only two arguments; a third argument for this call is not shown (?).
- V: the new state is written to block +0x18 after that call and before the selector runs.
- V: the selector is called with the new state id and returns the new handler. For the System agent the selector indexes the table at `off_14070DF40`, whose entries 0..6 are its state handlers.
- V: the returned handler is stored at block +0x08 and then tail-called as handler(owner, 0, 0) - the enter phase; the function does no further work.
- V: phase 1 is not run here. The agent's per-frame update virtual calls the current handler with (owner, 1, the qword stored at `g_Application`+1160): System slot 1 at 0x140181EB0 and SaveLoad slot 1 at 0x140182EDC.
- V: neither the old nor the new state value is passed to a handler; only the selector receives the new state value.
- I: the phases mean exit (2), per-frame (1) and enter (0), resting on how the handlers branch: UIAgentFFTOSystem_StateExitGame sets the quit byte on phase 2, waits for the fade and re-enters state 0 on phase 1, and frees the add-ons plus starts the fade on phase 0.
- ?: what a state id outside the selector's table does; the selector indexes the table without a bounds test and no caller was seen doing it.

## Referenced by

- Appears in flows: [UIAgentLifecycle](../flows/UIAgentLifecycle.md)
- Called by: [UISaveLoad_OnEvent](UISaveLoad_OnEvent.md), [UISaveLoad_Open](UISaveLoad_Open.md), [UISaveLoad_StateEnter](UISaveLoad_StateEnter.md), [UISaveLoad_StateSourcePick](UISaveLoad_StateSourcePick.md), [sub_140183658](sub_140183658.md), [sub_1401839E4](sub_1401839E4.md)

## Notes

Read from the function, its callers and the System/SaveLoad constructors. +0x48 is not the state field of this function's block; +0x48 is where the System and SaveLoad agents embed the block. The state id is block +0x18 (agent +0x60). The per-frame phase 1 is delivered by the agent update virtual, not by this function.

## Open questions

The 32-byte control block has no struct record; besides UIAgentFFTOSystem (+0x48) and UIAgentFFTOSaveLoad (+0x48 and +0x68), which agents embed one was not mapped.
