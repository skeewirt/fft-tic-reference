# UIAgentCursor_Show

- **Address:** `0x1401D2EF4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentCursor_Show(UIAgentCursor *agent)`
- **Callers:** UI_FrameUpdate, UIAgentCursor_PopRequest and about 30 other code paths (sub_1400FB3B0, sub_140119688, sub_140134B54, sub_140136654, Boot_Update, ...)
- **Callees:** UIAddonFingerCursor_PlayLoop

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Asks the finger cursor to appear and to restart its Loop animation. In the agent's normal state the restart is deferred to the start of the next UI frame.

## Behavior

- V: when agent+128 is 1 the call only sets agent+128 to 2 (a pending show); nothing else happens yet.
- V: otherwise (agent+128 is 0 or 2) and when the agent has its addon (agent+64) it calls UIAddonFingerCursor_PlayLoop(agent+64) at once.
- V: UI_FrameUpdate calls this function again at the start of a frame when agent+128 is 2, which takes the second branch. A show request therefore ends in a PlayLoop at the start of the next frame (a request made while one is already pending also plays the Loop at once), and the bob restarts from frame 0 each time.
- V: none of JobTree_Ctor, JobTree_RefreshAddon, JobTree_OnEvent, JobTree_OnFocusChange, JobTree_HandleInput, JobTree_OnCursorEnter, JobTree_OnCursorLeave or JobTree_SetPanelRecord refers directly to the addon manager or to a cursor function (decompile text search).
- I: the Job Tree code does not restart the bob itself; a call through a helper was not ruled out.

## State touched

- Calls: [UIAddonFingerCursor_PlayLoop](UIAddonFingerCursor_PlayLoop.md)
- Reads: [UIAgentCursor.show_state](../structs/UIAgentCursor.md#show_state), [UIAgentCursor.addon](../structs/UIAgentCursor.md#addon)
- Writes: [UIAgentCursor.show_state](../structs/UIAgentCursor.md#show_state)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Called by: [Battle_InitScene](Battle_InitScene.md), [Boot_Update](Boot_Update.md), [FreeCursor_StepFromSticks](FreeCursor_StepFromSticks.md), [UIAgentCursor_PopRequest](UIAgentCursor_PopRequest.md), [UI_FrameUpdate](UI_FrameUpdate.md), [sub_140136654](sub_140136654.md)

## Notes

The name is ours (IDB: sub_1401D2EF4). The agent is the second element of the addon manager's agent vector (global qword_143CD9DA8, vector at +16, element 1).

## Open questions

? Which show request is in force when the Job Tree opens (the hand arrives through the screen that opens it). Read the Loop clock of the cursor's main component live across a Job Tree entry to see whether it restarts.
